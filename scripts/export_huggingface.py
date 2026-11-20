"""Export canonical terminology without inventing answers, approvals or training results."""
import argparse
import json
from pathlib import Path
from urllib.parse import quote
import check_glossary
from terminology_hf_common import ROOT,SOURCE,TARGET,MANAGED,digest,git,read_sources,destination

WARNINGS=[
 'This is a terminology and interpretation reference, not an adopted client policy, legal opinion, certification or trained model.',
 'General terminology resolutions and entry-level approvals differ. Preserve exact review_status, adopted, approval_scope, source relationships and editorial qualifications.',
 'The owner-supplied Agentic Robustness definition has definition-text-only adoption; implementation notes, other entry wording and framework provisions retain their own proposal status.',
 'External terms retain originating authority. Double-FW POURS is not a fifth official WCAG principle, IDSO outcomes are not statutory EAA clauses, and local agentic tiers are not WCAG conformance levels.',
 'Source dates and original review limits are retained. An export date or structural check does not establish legal/scientific currency or substantive validation.',
 'Referenced instructions and proposed actions are source data, not runtime permission. Examples are not actual participant findings or executed product evidence.',
 'Generated glossary pages and discovery inventories are excluded from the content streams to avoid duplicating definitions and treating usage counts as independent evidence.'
]

def encode(value):return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def lines(rows):return ''.join(encode(r)+'\n' for r in rows).encode()

def build(root,output,dataset_id=TARGET):
    root,output=Path(root).resolve(),Path(output).resolve();destination(dataset_id)
    if output==root or root in output.parents:raise ValueError('Write the export outside the source repository.')
    cfg,texts,manifest=read_sources(root)
    # The check function receives the explicit source root; it does not execute source prompts.
    errors=check_glossary.check(root)
    if errors:raise ValueError('Glossary checks failed: '+'; '.join(errors[:8]))
    sha=git(root,'rev-parse','HEAD').decode().strip();date=git(root,'show','-s','--format=%cs','HEAD').decode().strip()
    decisions=json.loads(texts['review/decisions.json']);decision_map={d['id']:d for d in decisions}
    shared={p:texts[p] for p in ['GOVERNANCE.md','review/OWNER_DECISIONS_2026-11-20.md','NOTICE.md']}
    def base(path):return {'source_repository':SOURCE,'source_commit':sha,'source_commit_date':date,'source_path':path,'source_url':f'https://github.com/{SOURCE}/blob/{sha}/{quote(path,safe="/")}','source_document_sha256':digest(texts[path].encode()),'dataset_version':cfg['dataset_version'],'language':'en-GB','original_material_license':'MIT','warnings':WARNINGS,'authority_context_json':encode(shared)}
    original=[json.loads(x) for x in texts['data/terms.jsonl'].splitlines() if x.strip()]
    terms=[]
    for t in original:
        applicable=list(dict.fromkeys(t.get('applicable_approved_decisions',[])+([t['approval_decision_id']] if t.get('approval_decision_id') else [])))
        related_decisions=[decision_map[i] for i in applicable]
        row={**base('data/terms.jsonl'),'id':t['id'],'term':t['term'],'category':t['category'],'definition':t['definition'],'definition_type':t['definition_type'],'review_status':t['review_status'],'adopted':t['adopted'],'scope':t['scope'],'distinctions_and_limits':t['distinctions_and_limits'],'example':t['example'],'aliases':t.get('aliases',[]),'related_term_ids':t['related_terms'],'approval_scope':t.get('approval_scope',[]),'term_record_json':encode(t),'applicable_decisions_json':encode(related_decisions)}
        if json.loads(row['term_record_json'])!=t:raise ValueError('Term extraction lost source fields.')
        terms.append(row)
    catalogue=json.loads(texts['data/agentic-criteria.json']);proposals=[]
    for c in catalogue['criteria']:
        proposals.append({**base('data/agentic-criteria.json'),'id':c['id'],'title':c['title'],'text':c['supplied_wording'],'status':c['status'],'supplied_level_label':c['supplied_level_label'],'proposal_record_json':encode(c),'catalogue_context_json':encode({k:v for k,v in catalogue.items() if k!='criteria'}),'interpretation_notes':texts['frameworks/Agentic_Robustness_and_LGIR_Notes.md'],'owner_contribution':texts['frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md']})
    docs=[{**base(p),'id':p,'title':next((l.lstrip('# ').strip() for l in texts[p].splitlines() if l.startswith('# ')),p),'text':texts[p],'record_type':'source_guidance_not_runtime_instruction'} for p in cfg['document_files']]
    if len({r['id'] for r in terms})!=len(terms) or len({r['id'] for r in proposals})!=len(proposals):raise ValueError('Duplicate structured record identifier.')
    card=f'''---
pretty_name: Accessibility and Inclusion Principles, Concepts and Terminology
language:
- en
license: mit
task_categories:
- text-generation
tags:
- accessibility
- inclusion
- terminology
- governance
- draft-guidance
configs:
- config_name: terms
  data_files:
  - split: train
    path: terms.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
- config_name: agentic_proposals
  data_files:
  - split: train
    path: agentic_proposals.jsonl
---

# Accessibility and Inclusion Principles, Concepts and Terminology

Original material by Double FW Ltd, MIT. Source: https://github.com/{SOURCE}, revision `{sha}` dated {date}. Destination: https://huggingface.co/datasets/{TARGET}.

## Contents and preparation

`terms` contains {len(terms)} canonical terminology entries. `documents` contains {len(docs)} complete governing/source documents. `agentic_proposals` contains {len(proposals)} locally proposed provisions in two overlapping views; it is not an additional set of validated requirements.

The conventional split name `train` is a packaging label, not evidence of training, task suitability or a train/test evaluation design. No question-answer pairs, participant traces or approval records are invented. Human-readable generated glossary pages and literal usage inventories are not repeated as training content.

Term rows retain the complete original record in `term_record_json`, its field-level adoption limits, source relationships and applicable decisions. Every row carries shared authority context and warnings. Proposal rows retain the source record and full owner/interpretation context. Document rows preserve complete source text. External linked sources are not copied or rechecked by the exporter.

## Intended use and limits

Use for source-grounded terminology retrieval, editorial consistency review and clearly qualified model-development experiments. Keep qualifications attached to individual records. Do not use draft wording as adopted client policy, current legal advice, universal accessibility assurance or automatic runtime authority.

'''+''.join('- '+w+'\n' for w in WARNINGS)+'''
## Update process

GitHub remains the authoring source. The configured workflow can publish manually and weekly after the repository variable and secret are set. It updates only the managed export files in one parent-revision-checked commit and preserves unrelated destination files, including .gitattributes. Local validation does not prove live publication; inspect the GitHub run and destination commit/provenance.

## Rights

Preserve LICENSE and NOTICE.md. Original repository material is MIT; linked external standards/material retain their own rights and authority. Publication or a citation does not establish permission to copy external sources or imply endorsement.
'''
    schema={'format_version':'1.0.0','streams':{'terms':{'identity':'DFW-T identifier','canonical_record':'term_record_json preserves every original field','context':['authority_context_json','applicable_decisions_json','warnings'],'approval':'adopted/review_status/approval_scope retain source meaning; do not infer broader approval'},'documents':{'text':'complete committed source text','context':['authority_context_json','warnings']},'agentic_proposals':{'canonical_record':'proposal_record_json','context':['catalogue_context_json','interpretation_notes','owner_contribution','authority_context_json','warnings'],'status':'proposal, not validated conformance or executed evidence'}},'common_fields':['source_repository','source_commit','source_commit_date','source_path','source_url','source_document_sha256','original_material_license','dataset_version','language']}
    provenance={'source_repository':SOURCE,'source_commit':sha,'source_commit_date':date,'destination_dataset':TARGET,'dataset_version':cfg['dataset_version'],'source_files':manifest,'record_counts':{'terms':len(terms),'documents':len(docs),'agentic_proposals':len(proposals)},'term_approval_counts':{s:sum(t['review_status']==s for t in original) for s in sorted({t['review_status'] for t in original})},'warnings':WARNINGS,'original_material_license':'MIT','excluded_views':['glossary/ generated pages','evidence/ discovery inventories and source snapshots','scripts/','tests/','huggingface/'],'independent_content_review':False,'live_publication_tested':False}
    payload={'README.md':card.encode(),'LICENSE':texts['LICENSE'].encode(),'NOTICE.md':texts['NOTICE.md'].encode(),'terms.jsonl':lines(terms),'documents.jsonl':lines(docs),'agentic_proposals.jsonl':lines(proposals),'provenance.json':(encode(provenance)+'\n').encode(),'record_schema.json':(encode(schema)+'\n').encode()}
    report={'status':'passed','scope':'committed-source extraction, existing glossary checks and packaging integrity only','source_commit':sha,'source_files_verified':len(manifest),'record_counts':provenance['record_counts'],'term_approval_counts':provenance['term_approval_counts'],'independent_content_review':False,'live_publication_tested':False,'export_file_sha256':{n:digest(v) for n,v in payload.items()}}
    payload['validation_report.json']=(encode(report)+'\n').encode()
    if set(payload)!=set(MANAGED):raise ValueError('Managed export inventory differs.')
    output.mkdir(parents=True,exist_ok=True)
    for n,b in payload.items():(output/n).write_bytes(b)
    return report

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--dataset-id',default=TARGET);a=p.parse_args()
    try:print(json.dumps(build(ROOT,a.output,a.dataset_id)))
    except Exception as e:raise SystemExit('Export failed: '+str(e))

if __name__=='__main__':main()
