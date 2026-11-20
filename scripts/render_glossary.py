"""Render readable views from the canonical proposed terminology records."""
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def slug(text):
    return re.sub(r'[^a-z0-9]+','-',text.lower()).strip('-')

def render():
    terms=[json.loads(line) for line in (ROOT/'data/terms.jsonl').read_text().splitlines() if line.strip()]
    grouped=defaultdict(list)
    for term in terms:grouped[term['category']].append(term)
    paths={t['id']:f"{slug(t['category'])}.md#{t['id'].lower()}" for t in terms}
    names={t['id']:t['term'] for t in terms}
    out=ROOT/'glossary';out.mkdir(exist_ok=True)
    index=['# Glossary index','','Version 0.2.0 · Scoped owner decisions recorded · 20 November 2026','','Seven original terminology resolutions are approved, and decision 6 has an owner-supplied definition. Only that exact definition has entry-level adoption; other wording and the LGIR framework remain proposed. Source meanings and qualifications remain in force. [Start here](../START_HERE.md).','','## Browse by topic','']
    for group,entries in grouped.items():
        name=slug(group)+'.md'
        index.append(f'- [{group}]({name}) — {len(entries)} entries')
        lines=[f'# {group}','','Read each entry’s status. Only the unchanged owner-supplied Agentic Robustness definition has entry-level adoption; other wording remains proposed. Quoted standard titles and external meanings retain their source authority.','','[Alphabetical index](README.md) · [Review decisions](../review/DECISIONS.md)','','']
        for t in entries:
            status='Approved definition text only; editorial qualifications/examples proposed' if t['adopted'] else 'Proposed for owner review'
            lines.extend([f"<a id=\"{t['id'].lower()}\"></a>",f"## {t['term']}",'',f"**Reference:** {t['id']} · **Status:** {status} · **Basis:** {t['definition_type'].replace('_',' ')}",'',t['definition'],'',f"**Scope:** {t['scope']}",'',f"**Distinctions and limits:** {t['distinctions_and_limits']}",'',f"**Example:** {t['example']}",''])
            if t['adopted']:lines.extend([f"**Definition approval:** {t['approved_by']} · {t['approval_date']} · {t['approval_decision_id']}. [Owner decision record](../review/OWNER_DECISIONS_2026-11-20.md).",''])
            if t.get('applicable_approved_decisions'):lines.extend(['**Applicable approved terminology resolution:** '+', '.join(t['applicable_approved_decisions'])+'. This does not approve all entry wording. [Decision register](../review/DECISIONS.md).',''])
            if t['aliases']:lines.extend(['**Also encountered as:** '+ '; '.join(t['aliases']),''])
            if t.get('source_identifier'):lines.extend([f"**Owning-source identifier:** {t['source_identifier']}. Keep its namespace; the glossary reference does not replace it.",''])
            lines.append('**Source context:**')
            lines.append('')
            for s in t['sources']:
                label=s.get('repository',s.get('title','External primary reference'))
                if 'path' in s:label+=' / '+s['path']
                link='../'+s['url'] if s.get('source_type')=='owner_contribution' else s['url']
                lines.append(f"- [{label}]({link})")
                if 'usage_evidence' in s:
                    e=s['usage_evidence'];lines.append(f"  - Context located at line {e['line']}, under “{e['heading']}”. This supports interpretation; it is not approval of this definition.")
            lines.append('')
            if t['related_terms']:
                lines.extend(['**See also:** '+', '.join(f'[{names[x]}]({paths[x]})' for x in t['related_terms']), ''])
        (out/name).write_text('\n'.join(lines)+'\n')
    index.extend(['','## Alphabetical index','','| Term | Reference |','| --- | --- |'])
    for t in sorted(terms,key=lambda x:x['term'].casefold()):index.append(f"| [{t['term']}]({paths[t['id']]}) | {t['id']} |")
    (out/'README.md').write_text('\n'.join(index)+'\n')
    return len(terms)

if __name__=='__main__':print(f'Rendered {render()} terminology entries with recorded review states.')
