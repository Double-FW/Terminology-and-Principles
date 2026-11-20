# Agentic robustness and LGIR: owner contribution

**Supplied by Gareth Ford Williams · 20 November 2026**

The definition below is recorded as the owner's definition for decision 6. The guidelines and proposed agentic principles are retained as a user-supplied framework proposal, not a validated standard or implemented control set. Formatting has been normalised; the substantive supplied wording is retained. Editorial qualifications are separate in [implementation and interpretation notes](Agentic_Robustness_and_LGIR_Notes.md).

The A/AA labels below are supplied proposed local labels. They do not confer WCAG levels, legal compliance or agentic conformance. Likewise, “equivalent”, “analogous” and the mapping below describe the author's conceptual comparison; they do not establish formal equivalence with WCAG.

<a id="agentic-robustness-definition"></a>
## Agentic Robustness

Agentic systems, their underlying data, and their human-facing interfaces must be resilient, transparent, and interoperable enough to operate reliably across diverse models, shifting contexts, and human oversight mechanisms, both now and as capabilities evolve.

## Guideline 1: Epistemic & Data Integrity (Robustness of Training & Context Data)

Just as WCAG 4.1.1 historically ensured clean markup so parsers wouldn't break, agents require clean, uncorrupted, and well-attributed data so reasoning doesn't silently degrade.

- **1.1 Provenance & Grounding (Level A):** All ingested knowledge, retrieval-augmented context (RAG), and training inputs must carry verifiable metadata regarding source, recency, and confidence level, preventing agents from treating stale or unverified data as deterministic truth.
- **1.2 Distribution & Edge-Case Resilience (Level AA):** Models and retrieval pipelines must be evaluated against out-of-distribution inputs, adversarial prompt injections, and ambiguous phrasing so edge cases trigger graceful uncertainty rather than confident hallucination.

## Guideline 2: Execution & Architectural Compatibility (Robustness of Implementation)

Directly analogous to WCAG 4.1.2 (Name, Role, Value), an agent’s capabilities, tools, and internal states must be standardized and machine-legible across frameworks and future model upgrades.

- **2.1 Capability, Intent, State (Level A):** Every tool, API, and sub-agent action must programmatically expose its exact schema (capability), expected outcome (intent), and real-time execution status (state) using open, model-agnostic protocols (such as MCP or OpenAPI) rather than brittle prompt hacks.
- **2.2 Deterministic Guardrails & Graceful Degradation (Level A):** When a tool fails, an API times out, or confidence drops below threshold, the system must fail safely—preserving state, rolling back partial side effects, and falling back to deterministic logic or human escalation without corrupting downstream workflows.
- **2.3 Cross-Model Portability (Level AA):** Core business logic and state management must remain decoupled from specific foundation model quirks so the experience remains stable when swapped across different model providers or future versions.

## Guideline 3: Human-Agent Legibility & Co-Agency (Robustness of Assisted Human Experiences)

Directly analogous to WCAG 4.1.3 (Status Messages), humans supervising or collaborating with an agent need continuous, non-disruptive visibility into what the agent is doing and the power to intervene.

- **3.1 Ambient State & Reasoning Transparency (Level A):** Background actions, tool calls, and autonomous decisions must surface clear, real-time status updates and inspectable audit trails without hijacking the human’s primary workflow or cognitive focus.
- **3.2 Reversible Agency & Intervention Hooks (Level A):** Any action with real-world consequences must expose an explicit, accessible mechanism for the human to pause, override, modify parameters, or undo execution before or immediately after commitment.
- **3.3 Adaptive Calibration (Level AA):** The interface must communicate uncertainty and risk proportionally, requiring active human confirmation for high-stakes or ambiguous actions while allowing low-risk tasks to execute smoothly.

## Proposed agentic counterpart to POUR

We could really do with an agentic version of POUR that could be **L-G-I-R** (*Legible, Governable, Interpretable, Robust*)—or simply **Agentic POUR**:

- **Perceivable → Legible:** Can the human perceive the agent's presence, perception, and boundaries?
- **Operable → Governable:** Can the human direct, constrain, pause, and undo the agent's actions?
- **Understandable → Interpretable:** Can the human comprehend *why* the agent is acting and calibrate trust?
- **Robust → Resilient (Robust):** Can the system, data, and human-agent loop survive edge cases, model swaps, and failures?

<a id="lgir-legible"></a>
## Principle 1: Legible (Equivalent to Perceivable)

Agentic perception, capabilities, and state must be presented to human users in ways they can effortlessly detect and distinguish from human or deterministic system actions.

In WCAG, information cannot be invisible to a user's senses. In agentic UX, an agent’s presence, data sources, and current activity cannot be hidden in a "black box."

- **1.1 Agentic Attribution & Provenance (Level A):** Outputs generated, synthesized, or modified by an agent must be visually and programmatically distinguishable from deterministic system states and human-authored content, with direct links to underlying source data.
- **1.2 Scope & Capability Signaling (Level A):** Before delegation, the interface must clearly expose what tools, permissions, and context the agent can currently access (and what it cannot see).
- **1.3 Ambient Status & Multi-Modal Feedback (Level AA):** Long-running or background agent tasks must communicate live progress, waiting states, and completion through non-intrusive status indicators that work across visual, auditory, and assistive interfaces.

<a id="lgir-governable"></a>
## Principle 2: Governable (Equivalent to Operable)

Human operators must be able to steer, constrain, interrupt, and reverse agentic workflows at any point without requiring specialized technical expertise.

In WCAG, users must be able to operate the interface via keyboard, pointer, or voice without traps. In agentic UX, users must never be trapped in an autonomous loop they cannot steer or stop.

- **2.1 Interruptibility & Kill-Switches (Level A):** Every active agent execution loop must provide an immediate, low-latency mechanism to pause, cancel, or take over manual control without losing prior valid work.
- **2.2 Granular Permission & Blast-Radius Control (Level A):** Users must be able to define clear autonomy boundaries—specifying which actions can execute automatically, which require explicit approval, and hard limits on spending, data writes, or external communications.
- **2.3 Reversible Agency & Checkpoints (Level AA):** State-changing actions executed by an agent must automatically create state checkpoints, allowing the human to inspect diffs and roll back single steps or entire sessions cleanly.

<a id="lgir-interpretable"></a>
## Principle 3: Interpretable (Equivalent to Understandable)

Agentic reasoning, uncertainty, and behavioral rules must be predictable and comprehensible so humans can accurately calibrate their trust.

In WCAG, interfaces must behave predictably and help users avoid mistakes. In agentic UX, the primary failure mode is *misplaced trust*—either blindly accepting a hallucinated action or abandoning a useful agent due to erratic behavior.

- **3.1 Intent Preview & Plan Inspection (Level A):** For multi-step or high-impact tasks, the agent must articulate its proposed plan and expected side effects in plain language *before* committing irreversible actions.
- **3.2 Calibrated Confidence & Uncertainty Signaling (Level AA):** The interface must surface when the agent is operating on low-confidence retrieval, ambiguous instructions, or missing data—prompting human clarification rather than guessing silently.
- **3.3 Predictable Policy & Behavioral Consistency (Level AA):** Agents must adhere consistently to declared system rules and user preferences across sessions, surfacing an explicit explanation whenever a constraint prevents it from fulfilling a request.

<a id="lgir-robust"></a>
## Principle 4: Robust (Equivalent to Robust)

Agentic systems, their underlying data, and their human-facing interfaces must be resilient, transparent, and interoperable enough to operate reliably across diverse models, shifting contexts, and human oversight mechanisms—both now and as capabilities evolve.

- **4.1 Epistemic & Data Integrity (Level A / AA):** Training sets, RAG indexes, and runtime context must enforce provenance, freshness metadata, and adversarial input sanitization so edge cases produce safe uncertainty rather than corrupted reasoning.
- **4.2 Execution & Architectural Compatibility (Level A / AA):** Tools, APIs, and state machines must use open, model-agnostic schemas (*Capability, Intent, State*) with deterministic fallbacks and transactional rollbacks, ensuring stability across model upgrades or provider swaps.
- **4.3 Human-Agent Co-Agency Resilience (Level A / AA):** The human-in-the-loop layer must gracefully handle latency, partial failures, and shifting autonomy levels—ensuring human oversight remains effective even as agent speed and complexity scale.

## Summary Mapping: Web WCAG vs. Agentic AI

| WCAG Principle | Core Web Question | Agentic Principle | Core Agentic Question |
| --- | --- | --- | --- |
| Perceivable | Can the user see or hear the interface? | Legible | Can the user see what the agent sees, knows, and is doing? |
| Operable | Can the user navigate and control the UI? | Governable | Can the user steer, constrain, interrupt, and undo the agent? |
| Understandable | Does the UI make sense and prevent errors? | Interpretable | Does the user understand why the agent acted and when to trust it? |
| Robust | Does it work reliably across browsers & AT? | Robust | Does it survive bad data, tool failures, model swaps, and human error? |

The table preserves the supplied conceptual shorthand. It is not a complete definition of WCAG principles. See the separate notes for a broader-access rendering, including non-visual/non-auditory access and the limits of visibility, reversibility and future reliability claims.
