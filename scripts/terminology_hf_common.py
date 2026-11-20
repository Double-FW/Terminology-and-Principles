"""Committed-source and fixed-destination rules for terminology publication."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
SOURCE='Double-FW/Terminology-and-Principles'
TARGET='GarethFW/Accessibility_and_Inclusion_Principles_Concepts_and_Terminology'
MANAGED=('README.md','LICENSE','NOTICE.md','terms.jsonl','documents.jsonl','agentic_proposals.jsonl','provenance.json','record_schema.json','validation_report.json')
CONFIG='huggingface/export-config.json'

def digest(data):return hashlib.sha256(data).hexdigest()
def git(root,*args):return subprocess.check_output(['git','-C',str(root),*args])
def destination(value):
    if value!=TARGET:raise ValueError('HF_DATASET_ID must be '+TARGET+'.')
    return value

def committed(root,path):
    p=PurePosixPath(path)
    if p.is_absolute() or '..' in p.parts or any(x.startswith('.') for x in p.parts):raise ValueError('Invalid approved source path: '+path)
    info=git(root,'ls-tree','HEAD','--',path).decode().strip()
    if not info.startswith('100644 blob '):raise ValueError('Required source must be a committed regular file: '+path)
    sha=info.split()[2];data=git(root,'cat-file','blob',sha)
    if hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()!=sha:raise ValueError('Git source integrity failed: '+path)
    return data,{'path':path,'git_blob_sha':sha,'sha256':digest(data),'size_bytes':len(data)}

def read_sources(root=ROOT):
    raw,entry=committed(root,CONFIG);cfg=json.loads(raw)
    if cfg['source_repository']!=SOURCE:raise ValueError('Wrong source repository in export configuration.')
    destination(cfg['destination_dataset'])
    paths=cfg['source_files']
    if not isinstance(paths,list) or len(paths)!=len(set(paths)) or not all(isinstance(p,str) for p in paths):raise ValueError('Source allowlist must contain unique paths.')
    required={'data/terms.jsonl','data/agentic-criteria.json','data/term.schema.json','review/decisions.json','review/OWNER_DECISIONS_2026-11-20.md','GOVERNANCE.md','AGENTS.md','README.md','LICENSE','NOTICE.md','frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md','frameworks/Agentic_Robustness_and_LGIR_Notes.md'}
    if not required<=set(paths):raise ValueError('Required definitions, authority and framework qualifications must remain included.')
    if any(p.startswith(('glossary/','evidence/','scripts/','tests/','huggingface/')) for p in paths):raise ValueError('Generated views, discovery inventories and implementation files are not dataset source streams.')
    texts={};manifest=[entry]
    for path in paths:
        data,e=committed(root,path);text=data.decode('utf-8')
        if any(x in text for x in ['chatgpt.com/library?','account_id=personal','file_id=libfile_']):raise ValueError('Personal source-access locator in public export: '+path)
        texts[path]=text;manifest.append(e)
        working=Path(root)/path
        if not working.is_file() or working.is_symlink() or working.read_bytes()!=data:raise ValueError('Working source differs from the committed snapshot: '+path)
    if digest(texts['LICENSE'].encode())!=cfg['approved_license_sha256']:raise ValueError('Licence bytes changed; review before publication.')
    return cfg,texts,manifest

def public_source():
    request=urllib.request.Request('https://api.github.com/repos/'+SOURCE,headers={'User-Agent':'Double-FW-terminology-dataset-sync'})
    with urllib.request.urlopen(request,timeout=30) as response:info=json.load(response)
    if info.get('full_name')!=SOURCE or info.get('private') is not False or info.get('visibility')!='public':raise ValueError('Publishing requires the approved public GitHub source.')
