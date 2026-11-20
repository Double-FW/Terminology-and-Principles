# Maintain the glossary

## The current package

This edition has proposed definitions, source evidence and local integrity checks. A weekly/manual GitHub Action publisher is supplied for the owner-approved destination; setup and a successful run are required for publication. It has no deployed crawler or automatic approval process.

## Suggested weekly process, not yet scheduled

1. Compare the recorded source commits with current public source revisions.
2. Identify changes to the owning definition, qualifications, status and relevant cross-references. A changed file hash is a review signal, not proof the meaning changed.
3. Prepare proposed glossary updates and a readable explanation of their effects.
4. Ask the authorised owner to decide material changes. Retain disputes and evidence gaps.
5. Regenerate and check the glossary after accepted edits.
6. Publish a versioned release and, if configured later, export the reviewed records to the agreed Hugging Face dataset.
7. Verify the destination revision and source provenance after publication. A successful local export is insufficient.

Public sources can become unavailable or private. Stop treating unavailable content as retrievable evidence; retain a historical identifier and the fact of prior inspection where appropriate, but do not invent a replacement or copy private content into a public repository. Prefer appropriate public sources and disclose substitutions.

## For a maintainer or authorised agent

These commands use Python's standard library and run from the repository root:

```bash
python scripts/render_glossary.py
python scripts/check_glossary.py
```

Edit data/terms.jsonl for definitions. Rendered glossary files are derived views. Check results cover record shape, reference integrity, generated-view consistency and local navigation. They do not establish semantic agreement, external source freshness, real approval or effective model training.

## Expanding coverage

Add other public Double-FW repositories after the 27-repository baseline is reviewed. Add further specialist and regulatory terms, exact mappings between model namespaces, and source-specific exceptions based on inspected evidence. Do not assume that 168 entries cover every term or that candidate usage counts prove agreement.

Before a Hugging Face release, agree whether draft/disputed entries should be excluded or published in explicitly separate views. Preserve all status and source-boundary fields in every exported record. MIT covers original glossary material; third-party material retains its rights.

## Implemented publication path

The weekly/manual dataset publisher and [setup guide](huggingface/SETUP.md) publish committed canonical terminology and selected guidance. They do not implement the source-monitoring proposals above. Token/destination configuration and a verified run remain necessary.
