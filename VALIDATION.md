# What was checked

20 November 2026 · Version 0.2.0

## Original baseline

The first edition captured 27 public repository revisions and checked 557 Markdown/licence blobs against Git hashes. It located 146 selected source-context passages and added ten brief external primary-source paraphrases. Literal discovery scanned 417 Markdown files and excluded 113 by a disclosed path rule.

This revision retains that baseline without claiming a new live audit. Twelve owner-contributed agentic entries have been added and marked not rescanned in the usage inventory.

## Revision checks

Result: the integrity checker and all eleven regression tests passed. This is structural verification, not framework effectiveness validation.

The checker covers 168 terminology records, one approved definition, source relationships, generated-view agreement, local navigation and 20 proposed provisions in two overlapping views. It checks that the approved definition matches the recorded answer exactly and that convention approval cannot be transferred to an arbitrary entry.

The regression suite includes seven original tests plus checks for silent changes to the approved definition, overextended convention approval, false WCAG equivalence of agentic tiers and an untracked change to the owner contribution.

Checks do not authenticate identity, validate the framework independently, test an agent/tool, establish legal compliance or prove universal robustness. Approval evidence is the actual response recorded in the owner decision document, not a generated signature.

W3C Parsing, Name/Role/Value and Status Messages explanations and a pinned MCP cancellation/architecture edition were read for the comparisons. The MCP edition is not asserted as latest. These references do not establish formal equivalence with LGIR.

## Repeat local checks

```bash
python scripts/render_glossary.py
python scripts/check_glossary.py
python -m unittest discover -s tests -v
```

No new remote repository, Hugging Face publication, schedule or operational control was created. See [source coverage](evidence/SOURCE_COVERAGE.md).
