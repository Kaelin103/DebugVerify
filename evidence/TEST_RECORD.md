# DebugVerify — Live AI Test Record

## Test 1: Initial Live AI Diagnosis

**Input code:**
```python
def add(a, b):
    return a - b

print(add(3, 2))
```

**Expected behaviour:** 5

**Observed behaviour:** 1

**Action:** The user clicked "Analyse my code" in Live AI mode.

**Expected system response:** Identify the mismatch between the intended addition and the subtraction implemented in the function.

**Actual result:** The AI identified `return a - b` as the likely cause and suggested `return a + b`. It also explained that the intended behaviour should be confirmed.

**Verification evidence:** The system displayed an independent static syntax check with `syntax_ok` and two top-level statements. It clearly stated that this check did not prove logical correctness.

**Result:** PASS — The prototype returned a relevant live AI diagnosis. The suggested fix was not automatically executed.

## Test 2: Feedback-driven Re-analysis

**User feedback:** "I am not sure whether the function should perform addition or subtraction. Please explain how I can verify the intended behaviour before changing the code."

**Action:** The user clicked "Request re-analysis".

**Expected system response:** Reconsider the original suggestion and provide ways to verify the intended behaviour.

**Actual result:** The AI advised the user to check the specification, documentation, tests and function usage before changing the code. It explained that a function name is a clue rather than proof of its intended behaviour.

**Verification evidence:** The updated response suggested manual tests, including `add(2, 3)` and `add(10, 4)`. The system continued to distinguish AI-generated hypotheses from independent static syntax checks.

**Result:** PASS — The AI response changed in response to user feedback. No user code was executed or automatically modified.

## Current Limitations

- The prototype does not execute user-submitted Python code.
- Static syntax checking cannot establish logical correctness.
- AI-generated explanations and verification steps are not independently verified.
- These tests demonstrate prototype functionality, not improved debugging accuracy among novice programmers.

## DebugVerify v2 — Additional Live AI Test (14 November 2026)

### Test 3: Live AI Multiplication Diagnosis

Input code:

    def multiply(a, b):
        return a + b

    print(multiply(3, 4))

Expected output: 12
Observed output: 7

The user submitted the code through Live AI mode.

The AI identified the mismatch between the intended
multiplication and the addition implemented in the function.

The interface displayed an independent Python AST syntax
check and distinguished syntax validity from logical correctness.

Result: PASS

Evidence:
- 05_v2_live_initial_diagnosis.png
- 06_v2_live_initial_verification.png

### Test 4: Feedback-driven Re-analysis

User feedback:

"I am not sure whether the function should perform addition
or multiplication. Please explain how I can verify the intended
behaviour using the task requirements and test cases."

The user selected Request re-analysis.

The system returned a revised AI response recommending
verification against task requirements and representative
test cases before accepting the suggested modification.

The retry decision was recorded in decisions.jsonl.

Result: PASS

Evidence:
- 07_v2_reanalysis_diagnosis.png
- 08_v2_reanalysis_verification.png
- decisions.jsonl

### Automated Unit Tests

Date: 14 November 2026

Seven tests passed successfully.

Result: PASS (7/7)
Exit code: 0

Evidence:
- V2_AUTOMATED_TEST_RESULTS.txt

### Scope of Validation

These results demonstrate the operation of the tested
prototype features. They do not establish that AI-generated
fixes are correct or that novice programmers learn more
effectively when using the system.

