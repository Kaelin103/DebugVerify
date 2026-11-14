# DebugVerify — A2 Interaction Storyboards

## Storyboard 1: Accepting a Verified Suggestion

Images:
- case1_01_diagnosis.png
- case1_02_accept.png

A novice programmer receives a suggestion to replace `return i` with `return values[i]`. The interface presents a code observation and a pre-recorded test. After checking the intended output, the user accepts the suggestion.

Design rationale: The system encourages users to examine evidence before trusting AI-generated advice.

## Storyboard 2: Rejecting Misleading AI Advice

Images:
- case2_01_diagnosis.png
- case2_02_reject.png

A simulated AI suggestion recommends changing `value > 0` to `value >= 0`. The recorded test shows that this would produce an incorrect result. The user rejects the suggestion.

Design rationale: Showing contradictory evidence helps users identify misleading debugging suggestions.

## Storyboard 3: Requesting Further Verification

Images:
- case3_01_diagnosis.png
- case3_02_retry.png

A novice programmer encounters a missing import. The system identifies several possible explanations and recommends comparing the original response with the saved code. The user requests further analysis.

Design rationale: The interface communicates uncertainty and gives users control over the next action.

## Prototype limitations

These three scenarios are recorded examples, not live model outputs. Recorded tests are prepared in advance and are not executed by the prototype. Decisions are logged, but code files are not changed. Re-analysis in recorded mode logs the request only. Live AI mode supports model-generated responses and feedback-based re-analysis.
