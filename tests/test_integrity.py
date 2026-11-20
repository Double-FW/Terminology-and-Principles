import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from check_glossary import check

class IntegrityRegressions(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)/'repo'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('__pycache__','.git'))
    def tearDown(self):self.temp.cleanup()
    def change_record(self,mutator):
        p=self.root/'data/terms.jsonl';rows=[json.loads(l) for l in p.read_text().splitlines()];mutator(rows[0]);p.write_text(''.join(json.dumps(r)+'\n' for r in rows))
    def test_valid_draft(self):self.assertEqual([],check(self.root))
    def test_false_approval_is_rejected(self):
        self.change_record(lambda r:r.update(review_status='approved',adopted=True,approved_by='Invented approval',approval_date='2026-11-20'))
        self.assertTrue(any('approval lacks' in e for e in check(self.root)))
    def test_dangling_term_is_rejected(self):
        self.change_record(lambda r:r.update(related_terms=['DFW-T9999']))
        self.assertTrue(any('dangling' in e for e in check(self.root)))
    def test_changed_source_hash_is_rejected(self):
        self.change_record(lambda r:r['sources'][0].update(blob_sha='0'*40))
        self.assertTrue(any('revision/hash' in e for e in check(self.root)))
    def test_lost_qualification_is_rejected(self):
        self.change_record(lambda r:r.update(distinctions_and_limits=''))
        self.assertTrue(any('empty distinctions' in e for e in check(self.root)))
    def test_broken_local_navigation_is_rejected(self):
        p=self.root/'README.md';p.write_text(p.read_text()+'\n[Missing](missing.md)\n')
        self.assertTrue(any('missing local destination' in e for e in check(self.root)))
    def test_stale_generated_view_is_rejected(self):
        p=self.root/'glossary/foundations.md';p.write_text(p.read_text()+'\nUntracked change.\n')
        self.assertTrue(any('Stale generated view' in e for e in check(self.root)))
    def test_approved_definition_cannot_be_silently_rewritten(self):
        p=self.root/'data/terms.jsonl';rows=[json.loads(l) for l in p.read_text().splitlines()]
        next(r for r in rows if r['adopted'])['definition']+=' Guaranteed forever.'
        p.write_text(''.join(json.dumps(r)+'\n' for r in rows))
        self.assertTrue(any('differs from owner decision' in e for e in check(self.root)))
    def test_convention_approval_does_not_approve_arbitrary_entry(self):
        self.change_record(lambda r:r.update(review_status='approved',adopted=True,approved_by='Gareth Ford Williams',approval_date='2026-11-20',approval_decision_id='D01',approval_scope=['definition']))
        self.assertTrue(any('exceeds recorded scope' in e for e in check(self.root)))
    def test_agentic_tiers_do_not_become_wcag_equivalence(self):
        p=self.root/'data/agentic-criteria.json';d=json.loads(p.read_text());d['criteria'][0]['wcag_equivalence']=True;p.write_text(json.dumps(d))
        self.assertTrue(any('falsely promoted' in e for e in check(self.root)))
    def test_owner_source_change_requires_provenance_update(self):
        p=self.root/'frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md';p.write_text(p.read_text()+'\nChanged source.\n')
        self.assertTrue(any('owner source hash mismatch' in e for e in check(self.root)))

if __name__=='__main__':unittest.main()
