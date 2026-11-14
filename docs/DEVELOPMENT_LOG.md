# DebugVerify — Development Log

## Project Objective

DebugVerify is an interactive research prototype designed to
support novice programmers in evaluating AI-generated debugging
suggestions rather than accepting them without verification.

The project follows the research direction established in A1:
supporting evidence inspection, uncertainty awareness, trust
calibration, and user control during AI-assisted debugging.

## Phase 1 — Initial Recorded Prototype

Implemented a four-stage interaction workflow:

1. Problem context
2. AI diagnosis
3. Verification evidence
4. User decision

Three pre-authored scenarios were prepared:

- Case 1: Correct debugging suggestion — Accept
- Case 2: Misleading debugging suggestion — Reject
- Case 3: Uncertain explanation — Request re-analysis

The prototype displayed labelled evidence and recorded user
decisions in a local JSONL file.

Recorded diagnoses and test results were prepared in advance.
They were not generated or executed dynamically.

## Phase 2 — Live AI Integration

Added optional provider-backed AI analysis through an
OpenAI-compatible HTTPS chat-completions endpoint.

Implemented:

- Editable Python code input
- Expected and observed behaviour fields
- Dynamic AI diagnosis
- Suggested changes and uncertainty explanations
- Feedback-driven re-analysis

The Live AI workflow was tested locally on 14 November 2026
using a Volcengine Ark-hosted model.

## Phase 3 — Independent Syntax Checking

Added Python AST-based static syntax checking using ast.parse().

This check parses the submitted code without executing it.

It can identify syntax errors but cannot establish whether
a suggested fix is logically correct.

AI-generated explanations and suggested tests remain
unverified model outputs.

## Phase 4 — Validation and Evidence

Three recorded scenarios were exercised through the interface.

Live AI testing included:

- Initial diagnosis of an addition-versus-multiplication error
- Verification evidence display
- User feedback requesting clarification
- Feedback-driven AI re-analysis
- JSONL decision logging

Eight screenshots were saved in the evidence directory.

Seven automated unit tests passed on 14 November 2026.
The test process exited with code 0.

Supporting files:

- evidence/TEST_RECORD.md
- evidence/V2_AUTOMATED_TEST_RESULTS.txt
- evidence/01_live_initial_diagnosis.png
- evidence/02_live_initial_verification.png
- evidence/03_reanalysis_diagnosis.png
- evidence/04_reanalysis_verification.png
- evidence/05_v2_live_initial_diagnosis.png
- evidence/06_v2_live_initial_verification.png
- evidence/07_v2_reanalysis_diagnosis.png
- evidence/08_v2_reanalysis_verification.png

## AI Assistance Disclosure

ChatGPT assisted with code generation, implementation changes,
test scaffolding, documentation, and design explanations.

The student configured and ran the prototype locally,
tested the recorded scenarios and Live AI interactions,
reviewed the outputs, and retained evidence of the results.

The recorded cases are demonstrations rather than
empirical user-study findings.

## Known Limitations

- No execution of user-submitted Python code
- No automatic application of suggested fixes
- No guarantee that AI-generated suggestions are correct
- Recorded mode does not perform live AI re-analysis
- External model responses may be inaccurate or unavailable
- No empirical evidence of improved novice learning outcomes

## Current Status

Local interactive research prototype with recorded
demonstrations, optional Live AI analysis, feedback-driven
re-analysis, AST-based syntax checking, and decision logging.

Automated testing: 7/7 passed.

