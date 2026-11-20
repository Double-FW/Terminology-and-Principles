"""Check record integrity and generated/local references, not substantive truth."""
import json
import hashlib
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import unquote,urlsplit
import render_glossary

ROOT=Path(__file__).resolve().parents[1]

def check(root=ROOT):
    errors=[]
    def fail(message):errors.append(message)
    try:
        terms=[json.loads(line) for line in (root/'data/terms.jsonl').read_text().splitlines() if line.strip()]
        manifest=json.loads((root/'evidence/source-manifest.json').read_text())
        decisions=json.loads((root/'review/decisions.json').read_text())
        schema=json.loads((root/'data/term.schema.json').read_text())
        catalogue=json.loads((root/'data/agentic-criteria.json').read_text())
    except (OSError,ValueError) as e:return [f'Unreadable canonical data: {e}']
    source_map={(d['repository'],d['path']):d for d in manifest['scanned_documents']+manifest['excluded_from_literal_scan']}
    ids=[t.get('id') for t in terms]
    if len(set(ids))!=len(ids):fail('Duplicate term ID')
    labels=[t.get('term','').casefold() for t in terms]
    if len(set(labels))!=len(labels):fail('Duplicate preferred label')
    if len(manifest['repository_snapshots'])!=27:fail('Baseline repository snapshot count changed without a reviewed checker update')
    decision_map={d['id']:d for d in decisions}
    for t in terms:
        tid=t.get('id','MISSING')
        for field in schema['required']:
            if field not in t:fail(f'{tid}: missing {field}')
        if not re.fullmatch(r'DFW-T\d{4}',str(tid)):fail(f'{tid}: invalid ID')
        for field in ['term','category','definition','scope','distinctions_and_limits','example','record_version']:
            if not isinstance(t.get(field),str) or not t[field].strip():fail(f'{tid}: empty {field}')
        for field in ['definition_type','review_status']:
            if t.get(field) not in schema['properties'][field]['enum']:fail(f'{tid}: invalid {field}')
        if not isinstance(t.get('adopted'),bool):fail(f'{tid}: adopted must be boolean')
        if t.get('adopted')!=(t.get('review_status')=='approved'):fail(f'{tid}: inconsistent adoption state')
        if t.get('review_status')=='approved':
            decision=decision_map.get(t.get('approval_decision_id'))
            if not t.get('approved_by') or not t.get('approval_date') or not decision or decision.get('status')!='approved':fail(f'{tid}: approval lacks a recorded approved decision')
            elif tid not in decision.get('approved_term_ids',[]) or t.get('approval_scope')!=decision.get('approved_fields') or t.get('approved_by')!=decision.get('approved_by') or t.get('approval_date')!=decision.get('approval_date'):fail(f'{tid}: approval exceeds recorded scope')
            elif decision.get('approved_definition')!=t.get('definition'):fail(f'{tid}: approved definition differs from owner decision')
        elif t.get('approved_by') or t.get('approval_date'):fail(f'{tid}: non-approved entry claims approval')
        for related in t.get('related_terms',[]):
            if related not in ids or related==tid:fail(f'{tid}: dangling/self related reference {related}')
        if not isinstance(t.get('sources'),list) or not t['sources']:fail(f'{tid}: missing sources')
        for s in t.get('sources',[]):
            if s.get('source_type')=='owner_contribution':
                source_path=(root/s.get('path','')).resolve()
                if not source_path.is_relative_to(root.resolve()) or not source_path.is_file():fail(f'{tid}: missing owner source')
                elif hashlib.sha256(source_path.read_bytes()).hexdigest()!=s.get('content_sha256'):fail(f'{tid}: owner source hash mismatch')
                if unquote(s.get('url','')).split('#',1)[0]!=s.get('path') or not s.get('relationship'):fail(f'{tid}: incomplete owner source relationship')
            elif not s.get('url','').startswith('https://') or not s.get('relationship'):fail(f'{tid}: incomplete source relationship')
            if 'repository' in s:
                key=(s['repository'],s.get('path'));d=source_map.get(key)
                if not d or d['commit']!=s.get('commit') or d['blob_sha']!=s.get('blob_sha'):fail(f'{tid}: source revision/hash differs from snapshot')
                expected=f"https://github.com/{s['repository']}/blob/{s.get('commit')}/{s.get('path')}"
                if unquote(s['url'])!=expected:fail(f'{tid}: source URL differs from pinned source')
                if not s.get('interpretation_limits'):fail(f'{tid}: source interpretation limits missing')
        if t.get('definition_type')=='external_paraphrase' and not all(s.get('retrieval_status')=='content_retrieved' for s in t['sources']):fail(f'{tid}: external paraphrase lacks inspected primary source')
    criteria=catalogue.get('criteria',[]);criterion_ids={c.get('id') for c in criteria}
    if len(criteria)!=20 or len(criterion_ids)!=20:fail('Agentic proposal catalogue must retain its 20 distinct local references')
    for c in criteria:
        if not re.fullmatch(r'DFW-(?:AR|LGIR)-[1-4]\.[1-3]',c.get('id','')):fail('Invalid agentic criterion namespace')
        if c.get('wcag_equivalence') is not False or c.get('conformance_scheme_defined') is not False or c.get('status')!='owner_proposed_framework_unvalidated':fail('Agentic proposal falsely promoted to conformance or validation')
        if any(x not in criterion_ids for x in c.get('overlaps',[])):fail('Dangling agentic view relationship')
        p=(root/c.get('source_path','')).resolve()
        if not p.is_relative_to(root.resolve()) or not p.is_file():fail('Missing agentic criterion source')
        elif hashlib.sha256(p.read_bytes()).hexdigest()!=c.get('source_sha256'):fail('Agentic criterion source hash mismatch')
        elif c.get('supplied_wording','') not in p.read_text():fail('Agentic criterion wording differs from contribution')
    # Report invalid records before trying to render their broken references.
    if errors:return errors
    # Compare derived Markdown without modifying the user's working files.
    with tempfile.TemporaryDirectory() as temp:
        temp=Path(temp);(temp/'data').mkdir();shutil.copy(root/'data/terms.jsonl',temp/'data/terms.jsonl')
        old=render_glossary.ROOT
        try:render_glossary.ROOT=temp;render_glossary.render()
        finally:render_glossary.ROOT=old
        for p in (temp/'glossary').glob('*.md'):
            actual=root/'glossary'/p.name
            if not actual.exists() or actual.read_bytes()!=p.read_bytes():fail(f'Stale generated view: glossary/{p.name}')
        expected={p.name for p in (temp/'glossary').glob('*.md')}
        if {p.name for p in (root/'glossary').glob('*.md')}!=expected:fail('Unexpected generated glossary file set')
    # Check relative Markdown destinations and fragments outside fenced examples.
    for p in root.rglob('*.md'):
        fenced=False
        for line in p.read_text().splitlines():
            if line.lstrip().startswith(('```','~~~')):fenced=not fenced;continue
            if fenced:continue
            for raw in re.findall(r'\]\(([^)]+)\)',line):
                link=raw.strip().strip('<>');parsed=urlsplit(link)
                if parsed.scheme or parsed.netloc:continue
                target=(p.parent/unquote(parsed.path)).resolve() if parsed.path else p.resolve()
                if not target.is_relative_to(root.resolve()) or not target.is_file():fail(f'{p.relative_to(root)}: missing local destination {link}');continue
                if parsed.fragment and target.suffix=='.md':
                    text=target.read_text();anchors=set(re.findall(r'<a id="([^"]+)"',text))
                    for heading in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):anchors.add(re.sub(r'[^\w\- ]','',heading.lower()).replace(' ','-'))
                    if unquote(parsed.fragment) not in anchors:fail(f'{p.relative_to(root)}: missing anchor {link}')
    return errors

if __name__=='__main__':
    errors=check()
    if errors:
        print('\n'.join(errors));raise SystemExit(1)
    terms=[json.loads(l) for l in (ROOT/'data/terms.jsonl').read_text().splitlines() if l.strip()]
    print(json.dumps({'status':'passed','records':len(terms),'approved_records':sum(t['adopted'] for t in terms),'scope':'record integrity, source references, generated-view consistency and local navigation only','live_external_links_tested':False,'semantic_approval_tested':False}))
