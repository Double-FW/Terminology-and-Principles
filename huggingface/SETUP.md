# Weekly Hugging Face publication: terminology

Source: [Double-FW/Terminology-and-Principles](https://github.com/Double-FW/Terminology-and-Principles).

Destination: [Accessibility and Inclusion Principles, Concepts and Terminology](https://huggingface.co/datasets/GarethFW/Accessibility_and_Inclusion_Principles_Concepts_and_Terminology).

This setup publishes the current committed terminology. It does not scan the other 27 repositories for new meanings, approve definitions or train a model.

## 1. Put the sync files on GitHub

The workflow and scripts must be merged into this repository's main branch. If we are adding them together, give the connected GitHub account **Gareth-FW** collaborator access from [repository collaborators](https://github.com/Double-FW/Terminology-and-Principles/settings/access). An invitation must be accepted before it grants access. Alternatively upload the prepared files yourself, preserving paths, including `.github/workflows/huggingface-sync.yml`.

Do not rename `.github`. On a Mac, Command + Shift + . shows hidden items, but a file picker may still reject them. Uploading or creating the workflow through GitHub's web editor avoids the hidden-folder picker problem. This does not affect `.gitattributes`, which Hugging Face normally manages separately.

## 2. Set the ordinary repository variable

Open [GitHub Actions variables](https://github.com/Double-FW/Terminology-and-Principles/settings/variables/actions).

Create **HF_DATASET_ID**, with this exact value:

```text
GarethFW/Accessibility_and_Inclusion_Principles_Concepts_and_Terminology
```

It is the owner/dataset name, without the full URL or a trailing slash. It is not the token. If GitHub says the name already exists, edit the existing variable instead of creating another one.

## 3. Create or extend a narrowly scoped Hugging Face token

Open [Hugging Face token settings](https://huggingface.co/settings/tokens). Create a fine-grained token named **GitHub terminology sync**, or deliberately add this destination to an existing appropriately scoped token.

Under repository permissions, select only **GarethFW/Accessibility_and_Inclusion_Principles_Concepts_and_Terminology** and grant the read/write access needed for that selected repository. Do not select unrelated user-level write, inference, billing or organisation permissions. Some interfaces bundle associated permissions; the selected repository and effective scope must still be checked.

Create and copy the token. Do not paste it into chat, a repository file, an issue or the ordinary variable. If its full value can no longer be displayed, create a replacement and update the secret; do not try to recover it from Git history.

## 4. Add the GitHub secret

Open [GitHub Actions secrets](https://github.com/Double-FW/Terminology-and-Principles/settings/secrets/actions).

Choose New repository secret. Set **Name** to **HF_TOKEN** — underscore, not hyphen. Paste the token into Secret and save. If HF_TOKEN exists, use its update action. The value is hidden after saving; that is expected. Only the publishing step receives this secret.

## 5. Run the first update

Open [the terminology sync workflow](https://github.com/Double-FW/Terminology-and-Principles/actions/workflows/huggingface-sync.yml). Choose **Run workflow**, select **main**, and run it. If GitHub asks you to enable Actions, enable them for this repository. Open the new run and wait for the actual final result.

The workflow checks the setting, installs the pinned publishing dependency, runs glossary/integrity tests, exports committed content and publishes only after validation. A build alone is not evidence of a successful upload.

## 6. Verify the destination

Open [Hugging Face Files and versions](https://huggingface.co/datasets/GarethFW/Accessibility_and_Inclusion_Principles_Concepts_and_Terminology/tree/main).

Look for the updated dataset card, terms.jsonl, documents.jsonl, agentic_proposals.jsonl, provenance.json and validation_report.json, alongside LICENSE, NOTICE.md and record_schema.json. `.gitattributes` or other pre-existing files can remain. The workflow updates only its nine managed files; it does not delete unrelated files or change dataset visibility.

Check provenance.json against the source revision recorded in the GitHub run. The green workflow result, publishing summary and matching destination commit together establish publication. A report's live_publication_tested field stays false because local packaging checks are not a separate live integration test.

## Weekly updates

The configured schedule is **Mondays at 09:23 UTC**: 09:23 UK winter time and 10:23 UK summer time. GitHub scheduled starts can be delayed; this is not a guaranteed delivery time. The workflow also remains manually runnable. GitHub may disable scheduled workflows in inactive public repositories; check Actions if the weekly run stops.

Changes to canonical terms are reflected after they are committed and pass the glossary checks. Changes to approved document sources are also exported. New documents need a reviewed addition to huggingface/export-config.json. Generated glossary pages and discovery inventories are deliberately excluded from content streams. New or removed terms keep traceable IDs and are reported as additions/removals; publishing does not erase old releases, downloaded data or trained model knowledge.

If a token, variable, source licence, source visibility or destination access is wrong, the job should fail rather than silently publish elsewhere. Correct the identified setting and rerun. Do not share credentials or raw authentication responses when asking for help.
