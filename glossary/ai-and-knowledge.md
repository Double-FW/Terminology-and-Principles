# AI and knowledge

Read each entry’s status. Only the unchanged owner-supplied Agentic Robustness definition has entry-level adoption; other wording remains proposed. Quoted standard titles and external meanings retain their source authority.

[Alphabetical index](README.md) · [Review decisions](../review/DECISIONS.md)


<a id="dfw-t0092"></a>
## AI agent

**Reference:** DFW-T0092 · **Status:** Proposed for owner review · **Basis:** source grounded synthesis

A system that can pursue a bounded task using information and potentially tools or actions within granted authority.

**Scope:** Working Double-FW cross-repository terminology; preserve the owning source context.

**Distinctions and limits:** The label does not establish autonomy, competence or permission to act.

**Example:** Allow a retrieval agent to draft a report while retaining human release authority.

**Source context:**

- [Double-FW/Accessibility_Demographics / guides/agentic-workflow.md](https://github.com/Double-FW/Accessibility_Demographics/blob/d48e002627119d1cbcf8fb9d440021a7036c2bcb/guides/agentic-workflow.md)
  - Context located at line 2, under “”. This supports interpretation; it is not approval of this definition.

<a id="dfw-t0093"></a>
## Agentic workflow

**Reference:** DFW-T0093 · **Status:** Proposed for owner review · **Basis:** source grounded synthesis

A coordinated process in which AI systems perform specified tasks and handovers alongside appropriate human decisions.

**Scope:** Working Double-FW cross-repository terminology; preserve the owning source context.

**Distinctions and limits:** A workflow description is not evidence that software is deployed or permissions are granted.

**Example:** Document which steps are retrieval, drafting, review and authorised publication.

**Source context:**

- [Double-FW/Accessibility_Demographics / guides/agentic-workflow.md](https://github.com/Double-FW/Accessibility_Demographics/blob/d48e002627119d1cbcf8fb9d440021a7036c2bcb/guides/agentic-workflow.md)
  - Context located at line 2, under “”. This supports interpretation; it is not approval of this definition.

<a id="dfw-t0094"></a>
## Retrieval-augmented generation (RAG)

**Reference:** DFW-T0094 · **Status:** Proposed for owner review · **Basis:** source grounded synthesis

Generating an answer with information retrieved for the task from identified sources.

**Scope:** Working Double-FW cross-repository terminology; preserve the owning source context.

**Distinctions and limits:** Retrieval is not model training, and a matching snippet does not establish truth or source authority.

**Example:** Retrieve the owning definition together with its qualifications before drafting.

**Also encountered as:** RAG

**Source context:**

- [Double-FW/Accessibility_Demographics / guides/agentic-workflow.md](https://github.com/Double-FW/Accessibility_Demographics/blob/d48e002627119d1cbcf8fb9d440021a7036c2bcb/guides/agentic-workflow.md)
  - Context located at line 14, under “What agents can contribute”. This supports interpretation; it is not approval of this definition.

**See also:** [Training dataset](ai-and-knowledge.md#dfw-t0096)

<a id="dfw-t0095"></a>
## Knowledge base

**Reference:** DFW-T0095 · **Status:** Proposed for owner review · **Basis:** source grounded synthesis

An organised collection of information, relationships and guidance used to support questions or tasks.

**Scope:** Working Double-FW cross-repository terminology; preserve the owning source context.

**Distinctions and limits:** A collection's contents can have different authority and review status.

**Example:** Keep original sources, derived summaries and historical material distinguishable.

**Source context:**

- [Double-FW/Accessible-Chatbots / Accessible_Chatbot_Delivery_Methodologies.md](https://github.com/Double-FW/Accessible-Chatbots/blob/a1576b20e2519af0f79143f2984c242be2659701/Accessible_Chatbot_Delivery_Methodologies.md)
  - Context located at line 33, under “3\. M02 — Design complete interactions before implementation”. This supports interpretation; it is not approval of this definition.

<a id="dfw-t0096"></a>
## Training dataset

**Reference:** DFW-T0096 · **Status:** Proposed for owner review · **Basis:** source grounded synthesis

A collection prepared for use in a model training process, with documented content, provenance and permissions.

**Scope:** Working Double-FW cross-repository terminology; preserve the owning source context.

**Distinctions and limits:** Publishing a dataset on Hugging Face does not prove a model was trained on it or that it is suitable for every training objective.

**Example:** Describe the records and intended use before selecting a training method.

**Source context:**

- [Double-FW/Data_Ethics_and_Disability / Ethical and Inclusive Use of Data Relating to Disabled People.md](https://github.com/Double-FW/Data_Ethics_and_Disability/blob/77163fa48b6df5839e1294ec02797abf67c73980/Ethical%20and%20Inclusive%20Use%20of%20Data%20Relating%20to%20Disabled%20People.md)
  - Context located at line 421, under “AI Training and Accessibility Data”. This supports interpretation; it is not approval of this definition.

**See also:** [Retrieval-augmented generation (RAG)](ai-and-knowledge.md#dfw-t0094)

<a id="dfw-t0097"></a>
## Dataset card

**Reference:** DFW-T0097 · **Status:** Proposed for owner review · **Basis:** source grounded synthesis

Documentation explaining a dataset's contents, preparation, intended uses, limits and relevant rights.

**Scope:** Working Double-FW cross-repository terminology; preserve the owning source context.

**Distinctions and limits:** A card records claims and limitations; it is not independent certification of quality.

**Example:** Explain that exported guidance is not product-test evidence.

**Source context:**

- [Double-FW/Accessible-Chatbots / huggingface/SETUP.md](https://github.com/Double-FW/Accessible-Chatbots/blob/a1576b20e2519af0f79143f2984c242be2659701/huggingface/SETUP.md)
  - Context located at line 1, under “Weekly Accessible Chatbots dataset updates”. This supports interpretation; it is not approval of this definition.

<a id="dfw-t0098"></a>
## Source revision

**Reference:** DFW-T0098 · **Status:** Proposed for owner review · **Basis:** source grounded synthesis

The identified version of a source used for an interpretation or export.

**Scope:** Working Double-FW cross-repository terminology; preserve the owning source context.

**Distinctions and limits:** An immutable revision supports reproducibility but can still contain errors or outdated guidance.

**Example:** Record the Git commit and source path used to define the term.

**Source context:**

- [Double-FW/Accessible-Chatbots / huggingface/SETUP.md](https://github.com/Double-FW/Accessible-Chatbots/blob/a1576b20e2519af0f79143f2984c242be2659701/huggingface/SETUP.md)
  - Context located at line 21, under “What changes automatically”. This supports interpretation; it is not approval of this definition.

**See also:** [Source currency](evidence-and-assurance.md#dfw-t0069)

<a id="dfw-t0099"></a>
## Normative instruction

**Reference:** DFW-T0099 · **Status:** Proposed for owner review · **Basis:** source grounded synthesis

A requirement that has authority within an explicitly identified standard, policy or task context.

**Scope:** Working Double-FW cross-repository terminology; preserve the owning source context.

**Distinctions and limits:** Do not treat every occurrence of must in retrieved text as permission or runtime authority.

**Example:** Distinguish a quoted source requirement from the user's instructions to an agent.

**Applicable approved terminology resolution:** D08. This does not approve all entry wording. [Decision register](../review/DECISIONS.md).

**Source context:**

- [Double-FW/Inclusion-and-Accessibility-Policy / AGENTS.md](https://github.com/Double-FW/Inclusion-and-Accessibility-Policy/blob/66fa7132f2c38fbd13c629bf8c1b1dffbafb522d/AGENTS.md)
  - Context located at line 10, under “”. This supports interpretation; it is not approval of this definition.

<a id="dfw-t0156"></a>
## Model Context Protocol (MCP)

**Reference:** DFW-T0156 · **Status:** Proposed for owner review · **Basis:** external paraphrase

An open protocol connecting AI applications with external data, tools and workflows.

**Scope:** Brief orientation only; the originating organisation owns the authoritative meaning.

**Distinctions and limits:** MCP does not mean unrestricted permission, model training or guaranteed accessibility. MPC is not its acronym.

**Example:** Use MCP for the protocol and document the actual permitted capabilities.

**Also encountered as:** MCP

**Source context:**

- [External primary reference](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro)

