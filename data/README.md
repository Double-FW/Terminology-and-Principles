# Structured terminology records

**terms.jsonl is the editable canonical source.** Each UTF-8 line is one complete JSON record. The readable glossary is generated from it; edit records and regenerate rather than changing one representation alone.

| Field | Meaning |
| --- | --- |
| id | Stable glossary reference, independent of source identifiers |
| term, aliases, category | Preferred proposed label, encountered alternatives and browsing topic |
| definition, definition_type | Proposed explanation and whether it is synthesis, a framework summary, external orientation/paraphrase or a new convention |
| review_status, adopted | Explicit review/adoption state; one definition is approved within its recorded scope; other wording remains proposed |
| scope, distinctions_and_limits | Context and qualifications that must accompany retrieval |
| example | An illustrative use, not observed participant or product evidence |
| sources | Pinned supporting context or external primary reference, with relationship and retrieval notes |
| related_terms | Stable references for related entries; not claims of equivalence |
| source_identifier | The owning source's identifier where relevant, such as CP-01 or IDSO-01 |
| created, last_editorial_review | Record dates; not renewed legal/scientific verification dates |
| approved_by, approval_date | Empty until supported by an actual approval record |
| record_version, supersedes | Entry version and any replaced glossary reference |

The included schema supports record-shape checks. The standard-library checker checks key constraints without a third-party schema engine. Neither proves definitions are substantively right.

## Source evidence

Supporting source context is not necessarily a source-authored definition. usage_evidence records a located passage or heading and its line number. Excerpts are short context aids; inspect the linked source and its qualifications. Literal discovery counts are separate from these selected supporting relationships.

External summaries point to their primary sources and remain paraphrases. Do not treat a matching source phrase as approval of this glossary's definition, or an editorial date as legal currency.

## Training and retrieval boundary

The JSONL is a draft terminology view suitable for inspection and pipeline design. It is not a completed model-training dataset or evidence of a trained model. All qualifications remain part of each record. A later approved-only export must use explicit review decisions, not assumed approval from a Git merge.

## Version 0.2.0 additions

Records include approval_decision_id and approval_scope where relevant. Only DFW-T0157 has definition-field adoption under D06; its editorial notes remain proposed. A local owner-contribution source records its content hash, received date and relationship. The renderer resolves the root-relative source path for human pages.

agentic-criteria.json preserves twenty supplied provisions in overlapping DFW-AR and DFW-LGIR views. It retains wording and provisional local tier labels, explicit non-equivalence/non-conformance flags, source hash and proposed overlap relationships. It is a proposal catalogue, not executed test evidence. New owner terms have null usage counts, not invented zeros.
