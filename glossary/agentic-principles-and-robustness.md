# Agentic principles and robustness

Read each entry’s status. Only the unchanged owner-supplied Agentic Robustness definition has entry-level adoption; other wording remains proposed. Quoted standard titles and external meanings retain their source authority.

[Alphabetical index](README.md) · [Review decisions](../review/DECISIONS.md)


<a id="dfw-t0157"></a>
## Agentic Robustness

**Reference:** DFW-T0157 · **Status:** Approved definition text only; editorial qualifications/examples proposed · **Basis:** owner supplied definition

Agentic systems, their underlying data, and their human-facing interfaces must be resilient, transparent, and interoperable enough to operate reliably across diverse models, shifting contexts, and human oversight mechanisms, both now and as capabilities evolve.

**Scope:** Double-FW agentic system/data/interface and oversight lens; retain WCAG and other source-owned meanings separately.

**Distinctions and limits:** The definition text is owner-approved. Scope, examples and implementation qualifications are editorial proposals: define supported conditions and versions, protect oversight, and do not promise arbitrary future compatibility. This is distinct from WCAG robustness.

**Example:** Exercise a delayed, partially completed action and verify that data, execution status and human intervention remain dependable.

**Definition approval:** Gareth Ford Williams · 2026-11-20 · D06. [Owner decision record](../review/OWNER_DECISIONS_2026-11-20.md).

**Also encountered as:** agentic robustness

**Source context:**

- [Gareth Ford Williams: Agentic robustness and LGIR proposal / frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md](../frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md#agentic-robustness-definition)

**See also:** [Robust (WCAG)](standards-and-external-terms.md#dfw-t0152), [LGIR](agentic-principles-and-robustness.md#dfw-t0158), [Feeling Safe](experience.md#dfw-t0031), [Epistemic and data integrity](agentic-principles-and-robustness.md#dfw-t0162), [Capability, Intent, State](agentic-principles-and-robustness.md#dfw-t0163), [Graceful degradation](agentic-principles-and-robustness.md#dfw-t0164), [Cross-model portability](agentic-principles-and-robustness.md#dfw-t0165), [Human-agent co-agency resilience](agentic-principles-and-robustness.md#dfw-t0166)

<a id="dfw-t0158"></a>
## LGIR

**Reference:** DFW-T0158 · **Status:** Proposed for owner review · **Basis:** double fw framework

The proposed Double-FW agentic framework: Legible, Governable, Interpretable and Robust.

**Scope:** Double-FW agentic system/data/interface and oversight lens; retain WCAG and other source-owned meanings separately.

**Distinctions and limits:** A conceptual counterpart to POUR, not a WCAG amendment, equivalence claim or validated agentic conformance scheme. The framework remains proposed.

**Example:** Evaluate delegation through presence/state, control, understandable decisions and failure recovery.

**Also encountered as:** Agentic POUR (analogy only)

**Source context:**

- [Gareth Ford Williams: Agentic robustness and LGIR proposal / frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md](../frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md)

**See also:** [Agentic Robustness](agentic-principles-and-robustness.md#dfw-t0157), [POUR](standards-and-external-terms.md#dfw-t0148), [POURS](experience.md#dfw-t0108), [Legible (agentic)](agentic-principles-and-robustness.md#dfw-t0159), [Governable (agentic)](agentic-principles-and-robustness.md#dfw-t0160), [Interpretable (agentic)](agentic-principles-and-robustness.md#dfw-t0161)

<a id="dfw-t0159"></a>
## Legible (agentic)

**Reference:** DFW-T0159 · **Status:** Proposed for owner review · **Basis:** double fw framework

Agentic perception, capabilities, and state must be presented to human users in ways they can effortlessly detect and distinguish from human or deterministic system actions.

**Scope:** Double-FW agentic system/data/interface and oversight lens; retain WCAG and other source-owned meanings separately.

**Distinctions and limits:** Owner-proposed principle wording. Detectability must be evaluated across access needs; do not claim effortlessness for everyone or disclose protected context.

**Example:** Make agent involvement and meaningful progress available through the person’s supported access route.

**Source context:**

- [Gareth Ford Williams: Agentic robustness and LGIR proposal / frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md](../frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md#lgir-legible)

**See also:** [LGIR](agentic-principles-and-robustness.md#dfw-t0158)

<a id="dfw-t0160"></a>
## Governable (agentic)

**Reference:** DFW-T0160 · **Status:** Proposed for owner review · **Basis:** double fw framework

Human operators must be able to steer, constrain, interrupt, and reverse agentic workflows at any point without requiring specialized technical expertise.

**Scope:** Double-FW agentic system/data/interface and oversight lens; retain WCAG and other source-owned meanings separately.

**Distinctions and limits:** Owner-proposed principle wording. Clarify actual authority and timing; irreversible effects and remote cancellation limits need truthful disclosure and pre-commit controls.

**Example:** Show whether cancellation is requested, acknowledged or completed, with the remaining effects.

**Source context:**

- [Gareth Ford Williams: Agentic robustness and LGIR proposal / frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md](../frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md#lgir-governable)

**See also:** [LGIR](agentic-principles-and-robustness.md#dfw-t0158), [Reversible agency](agentic-principles-and-robustness.md#dfw-t0167)

<a id="dfw-t0161"></a>
## Interpretable (agentic)

**Reference:** DFW-T0161 · **Status:** Proposed for owner review · **Basis:** double fw framework

Agentic reasoning, uncertainty, and behavioral rules must be predictable and comprehensible so humans can accurately calibrate their trust.

**Scope:** Double-FW agentic system/data/interface and oversight lens; retain WCAG and other source-owned meanings separately.

**Distinctions and limits:** Owner-proposed principle wording. Explain decision factors and evidence without requiring hidden chain-of-thought or treating a generated explanation as an execution trace.

**Example:** Explain the action’s goal, relevant evidence, material constraints, uncertainty and outcome.

**Source context:**

- [Gareth Ford Williams: Agentic robustness and LGIR proposal / frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md](../frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md#lgir-interpretable)

**See also:** [LGIR](agentic-principles-and-robustness.md#dfw-t0158), [Calibrated uncertainty](agentic-principles-and-robustness.md#dfw-t0168)

<a id="dfw-t0162"></a>
## Epistemic and data integrity

**Reference:** DFW-T0162 · **Status:** Proposed for owner review · **Basis:** double fw framework

The proposed agentic robustness domain concerned with trustworthy handling of training, retrieval and runtime knowledge, including provenance, uncertainty and resistance to corrupted context.

**Scope:** Double-FW agentic system/data/interface and oversight lens; retain WCAG and other source-owned meanings separately.

**Distinctions and limits:** This synthesis is proposed. Metadata and sanitisation cannot guarantee truthful reasoning or defeat all prompt injection; missing provenance stays explicit.

**Example:** Keep source dates and qualifications attached to retrieved guidance and refuse to invent missing lineage.

**Source context:**

- [Gareth Ford Williams: Agentic robustness and LGIR proposal / frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md](../frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md)

**See also:** [Agentic Robustness](agentic-principles-and-robustness.md#dfw-t0157)

<a id="dfw-t0163"></a>
## Capability, Intent, State

**Reference:** DFW-T0163 · **Status:** Proposed for owner review · **Basis:** double fw framework

The proposed contract describing what an action can do, its intended effect and its actual execution state.

**Scope:** Double-FW agentic system/data/interface and oversight lens; retain WCAG and other source-owned meanings separately.

**Distinctions and limits:** This is a local conceptual pattern, not an established universal MCP or OpenAPI object or proof that declared intent will be achieved.

**Example:** Distinguish the permitted operation, expected change and observed partially completed status.

**Source context:**

- [Gareth Ford Williams: Agentic robustness and LGIR proposal / frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md](../frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md)

**See also:** [Agentic Robustness](agentic-principles-and-robustness.md#dfw-t0157)

<a id="dfw-t0164"></a>
## Graceful degradation

**Reference:** DFW-T0164 · **Status:** Proposed for owner review · **Basis:** double fw framework

A controlled response to reduced capability or failure that preserves appropriate safety, useful state and truthful communication of limitations.

**Scope:** Double-FW agentic system/data/interface and oversight lens; retain WCAG and other source-owned meanings separately.

**Distinctions and limits:** A deterministic fallback is not automatically safe. Unknown remote outcomes need reconciliation; disclose limits and escalate where required.

**Example:** After a timeout, check whether the payment committed before retrying.

**Source context:**

- [Gareth Ford Williams: Agentic robustness and LGIR proposal / frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md](../frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md)

**See also:** [Agentic Robustness](agentic-principles-and-robustness.md#dfw-t0157)

<a id="dfw-t0165"></a>
## Cross-model portability

**Reference:** DFW-T0165 · **Status:** Proposed for owner review · **Basis:** double fw framework

The proposed architectural objective of preserving defined service behaviour and oversight when supported models or providers change.

**Scope:** Double-FW agentic system/data/interface and oversight lens; retain WCAG and other source-owned meanings separately.

**Distinctions and limits:** Decoupling and common schemas help but do not guarantee unchanged behaviour; evaluate the actual replacement before release.

**Example:** Run the versioned action and recovery scenarios against the candidate model before switching.

**Source context:**

- [Gareth Ford Williams: Agentic robustness and LGIR proposal / frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md](../frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md)

**See also:** [Agentic Robustness](agentic-principles-and-robustness.md#dfw-t0157)

<a id="dfw-t0166"></a>
## Human-agent co-agency resilience

**Reference:** DFW-T0166 · **Status:** Proposed for owner review · **Basis:** double fw framework

The proposed ability of the human–agent working arrangement to retain effective control and oversight through latency, partial failures and changing autonomy.

**Scope:** Double-FW agentic system/data/interface and oversight lens; retain WCAG and other source-owned meanings separately.

**Distinctions and limits:** An oversight button is insufficient without accessible information, actual authority and enough opportunity to intervene.

**Example:** Check that the accountable operator can understand and constrain a paused workflow after a tool failure.

**Source context:**

- [Gareth Ford Williams: Agentic robustness and LGIR proposal / frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md](../frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md)

**See also:** [Agentic Robustness](agentic-principles-and-robustness.md#dfw-t0157)

<a id="dfw-t0167"></a>
## Reversible agency

**Reference:** DFW-T0167 · **Status:** Proposed for owner review · **Basis:** double fw framework

The proposed ability to inspect and reverse or safely compensate for agent-caused changes within defined boundaries.

**Scope:** Double-FW agentic system/data/interface and oversight lens; retain WCAG and other source-owned meanings separately.

**Distinctions and limits:** Reversible, compensatable and irreversible actions differ. A checkpoint cannot guarantee undo for an already sent message or committed external action.

**Example:** Preview an irreversible action before commitment and retain a truthful record of what can still be corrected.

**Source context:**

- [Gareth Ford Williams: Agentic robustness and LGIR proposal / frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md](../frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md)

**See also:** [Governable (agentic)](agentic-principles-and-robustness.md#dfw-t0160)

<a id="dfw-t0168"></a>
## Calibrated uncertainty

**Reference:** DFW-T0168 · **Status:** Proposed for owner review · **Basis:** double fw framework

Communication and handling of uncertainty appropriate to the evidence, task, risk and available evaluation.

**Scope:** Double-FW agentic system/data/interface and oversight lens; retain WCAG and other source-owned meanings separately.

**Distinctions and limits:** A model’s self-reported confidence is not automatically a calibrated probability. Separate source reliability, retrieval relevance, model uncertainty and action risk.

**Example:** Explain the missing evidence and seek the decision needed for the affected action while continuing independent authorised work.

**Source context:**

- [Gareth Ford Williams: Agentic robustness and LGIR proposal / frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md](../frameworks/Agentic_Robustness_and_LGIR_User_Proposal.md)

**See also:** [Interpretable (agentic)](agentic-principles-and-robustness.md#dfw-t0161)

