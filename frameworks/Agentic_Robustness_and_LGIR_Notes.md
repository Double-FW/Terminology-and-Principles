# Agentic robustness and LGIR: interpretation and implementation notes

**Editorial proposals · Version 0.2.0 · 20 November 2026**

Gareth supplied the [agentic robustness definition and framework proposal](Agentic_Robustness_and_LGIR_User_Proposal.md). The definition is recorded as his chosen answer to decision 6. The notes below clarify implementation questions; they are not presented as his approved wording, a deployed specification or tested success criteria.

## Name and scope

Use **LGIR — Legible, Governable, Interpretable, Robust** as the proposed primary name. “Agentic POUR” can be an explanatory analogy, not a claim that this framework is part of WCAG or replaces it. Retain WCAG's four principles for accessibility of the human-facing service itself. Retain POURS for Double-FW experience and brand questions; LGIR adds a distinct agentic governance and interaction lens.

The source proposal has eight detailed robustness provisions and twelve LGIR provisions. These are two related views, not twenty independent requirements to count together. The catalogue gives them separate namespaces and explicit many-to-many cross-references. No aggregate score or conformance level is defined.

## Preserve three distinct meanings of robustness

| Meaning | What to examine | What it does not establish |
| --- | --- | --- |
| WCAG robustness | Reliable interpretation of content by user agents, including assistive technology, within the applicable requirements | Reliable reasoning, safe tool execution or every person's confidence |
| Agentic robustness | Integrity of data/context, execution and the human–agent oversight loop across declared operating conditions and changes | WCAG conformance, unlimited interoperability or guaranteed future reliability |
| AI-system robustness in a specific law, standard or assurance regime | The exact externally defined meaning and applicability, inspected at the relevant version | Automatic equivalence to the Double-FW definition |

Feeling Safe remains a separate experience lens. A participant's reassurance and a system's actual security/reliability can diverge.

## Refine the POUR analogy without narrowing access

| WCAG principle | Brief orientation, not a replacement definition | LGIR lens | Practical question |
| --- | --- | --- | --- |
| Perceivable | Relevant information and controls can be perceived through appropriate access routes | Legible | Can the person identify agent involvement, available context, boundaries and meaningful state? |
| Operable | The interface and navigation can be operated | Governable | Can the authorised person direct and constrain the work and obtain effective intervention? |
| Understandable | Information and interface operation can be understood | Interpretable | Can the person understand intent, material decision factors, limits and uncertainty sufficiently for the decision? |
| Robust | Content can be interpreted reliably by user agents, including AT | Robust | Do data, execution and oversight remain dependable under the defined failure and change scenarios? |

Perception is broader than seeing or hearing: include relevant tactile and other access routes. “See what the agent sees” is a metaphor; do not imply that an agent has complete knowledge or require access to protected data. These relationships are analogies, not conformance mappings or proof that one principle satisfies the other.

## Proposed qualifications for the framework

### 1. Treat A and AA as local provisional labels

The owner contribution borrows A/AA labels. Use **proposed Double-FW tier A/AA**, never “WCAG Level A/AA” for these agentic provisions. The combined A/AA provisions have not yet been divided into separately testable obligations. A future assurance specification needs scope, applicability, test procedures, failure conditions, tolerances, evidence and a rule for levels. None has been validated here.

WCAG 4.1.1 Parsing was removed from WCAG 2.2. Its use in the contribution is a historical analogy, not a current WCAG 2.2 requirement. WCAG 4.1.2 and 4.1.3 likewise do not themselves require agent schemas, rollback or reasoning logs. [W3C on Parsing](https://www.w3.org/WAI/WCAG22/Understanding/parsing.html), [Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) and [Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html).

### 2. Separate provenance, currency and confidence

Record the granularity actually available: source/collection, revision, transformation, relevant dates, permitted use and uncertainty. Where historical training inputs cannot be individually attributed, record that limitation rather than inventing provenance or claiming complete traceability. Dataset-collection provenance and runtime RAG provenance can differ.

Source reliability, retrieval relevance, model uncertainty and action risk are different judgements. A model's self-reported confidence is not automatically a calibrated probability. Unknown dates or confidence must remain unknown. Define how freshness is assessed for the task, rather than treating a recent upload as current knowledge. Metadata alone cannot prevent false conclusions.

### 3. Defend trust boundaries, not just text cleanliness

Treat retrieved documents, tool results and user-supplied reference material as data with explicit authority limits. Input sanitisation can support protection but cannot be the sole defence against prompt injection. Combine constrained permissions, separation of instructions and untrusted content, output/action validation and representative adversarial evaluation. Passing selected cases cannot guarantee resistance to every attack.

### 4. Distinguish an interface contract from reliable execution

An open schema describes allowed structure; it does not prove that a tool will do what was intended. Capability, intended effect, authorisation, actual status and observed outcome need explicit representation. MCP and OpenAPI are enabling approaches, not interchangeable protocols or evidence of behavioural correctness. Where required information is supplied by an adapter or orchestrator, document that boundary.

Keep business rules and durable state outside model-specific prompt assumptions where appropriate. Nonetheless, model/provider changes can alter behaviour. Define supported combinations, versioned regression cases and release review before changing them. Do not promise identical performance across arbitrary models or future releases.

### 5. Make stop and rollback promises truthful

Distinguish **pause/cancel requested**, **acknowledged**, **stopped**, **completed**, **partially completed** and **outcome unknown**. A local kill switch cannot guarantee immediate cancellation of an already committed remote action. Define tolerances and the safe behaviour for the actual domain. The pinned [MCP cancellation specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/cancellation) allows for requests that cannot be cancelled or have already completed; it does not guarantee rollback.

Classify actions as reversible, compensatable or irreversible. Checkpoints do not unsend an email or reverse every payment. Protect valid work and prevent duplicate retries through appropriate transaction boundaries, idempotency, reconciliation and conflict-aware recovery. Use compensating action where safe and authorised; disclose residual consequences. For irreversible or high-impact actions, provide the required preview and authorisation before commitment.

A deterministic fallback can still be wrong or unsafe. Use only fallbacks evaluated for the defined conditions. Where outcomes are uncertain, reconcile or escalate rather than treating a timeout as proof that nothing happened. Do not simulate completed recovery in a status message.

### 6. Explain decisions without promising private internal reasoning

Expose a useful explanation: goal, relevant evidence, material constraints, decision factors, action summary, uncertainty and actual outcome. This is not a requirement to reveal hidden internal chain-of-thought or to present a generated rationale as a faithful execution trace.

Audit records should reflect actual events and distinguish predictions from observations. Make access proportionate to role; protect personal data, credentials, private source material and security-sensitive details. Direct public source links are not appropriate for every protected input. Offer authorised provenance summaries or controlled access instead.

### 7. Support effective, accessible co-agency

Identify the affected person, operator, supervisor and accountable decision-maker. These may be different people with different intervention rights. Governance does not grant every user unrestricted power over other people's data or organisational controls.

Provide meaningful status and actionable controls through supported accessible channels, with user preferences and controlled notification priority. Avoid compulsory simultaneous visual, auditory and haptic output, repeated live-region announcements or focus theft. Continuous visibility does not mean announcing every token or tool event. The operator also needs time, understandable information and the authority to intervene before oversight becomes nominal.

Use confirmation proportionately to risk, uncertainty, reversibility and actual authorisation. Clear existing authorisation can cover low-impact work; do not make every step a new approval request. A high-impact or materially changed action may need a specific preview and decision. When information is missing, ask for clarification only when needed for the affected action; continue independent authorised work.

Misplaced trust is an important failure mode, but its primacy depends on the service. Also evaluate exclusion, incorrect outcomes, unauthorised action, disclosure, resource exhaustion and other relevant harms; do not reduce safety or accessibility to trust ratings.

## Suggested delivery sequence

1. Adopt the owner-supplied definition as a glossary entry with its stated scope.
2. Review the LGIR names and these editorial qualifications as a framework proposal.
3. Define the user roles, operating envelope and measurable outcomes before designing levels or scores.
4. Build failure, ambiguity, attack and recovery scenarios across data, tools and oversight.
5. Evaluate with appropriate specialists and affected people; retain failures and unknowns.
6. Pilot the framework in a bounded real workflow before any conformance or effectiveness claim.

This package completes steps of documentation and structural checking. It does not implement or validate the controls, establish legal compliance, or create an operational monitoring service.
