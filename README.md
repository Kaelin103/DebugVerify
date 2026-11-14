# DebugVerify v2 — IIS Assignment 2

**Status:** Local interactive research prototype; three pre-authored recorded cases, optional live AI diagnosis and re-analysis, independent syntax-only check. No user code execution, automated patching, or correctness guarantee.

## Start (Windows PowerShell)

```powershell
cd E:\IIS\DebugVerify
.\start.ps1
```

Alternatively: `.\.venv\Scripts\python.exe app.py`. Open http://127.0.0.1:8000 . Stop with Ctrl+C. Python standard library only.

## Optional live AI

Supports an OpenAI-compatible **HTTPS chat-completions endpoint**. Provider/model compatibility varies. Set these environment variables in the *same PowerShell terminal* before starting:

```powershell
$env:DEBUGVERIFY_API_URL = "https://YOUR_PROVIDER/v1/chat/completions"
$env:DEBUGVERIFY_MODEL = "YOUR_MODEL_ID"
$env:DEBUGVERIFY_API_KEY = Read-Host "API key"
.\start.ps1
```

Do not paste your API key into code, GitHub, screenshots, or reports. Avoid uploading sensitive code to external providers. The model response is unverified and may be inaccurate. The `Read-Host` command avoids echoing the key into the command history, but entered text may be visible on screen; use `Read-Host -AsSecureString` with careful conversion if required by your environment. This app is intended for local use only (`127.0.0.1`).

## Interaction

- **Recorded cases:** select one of three prepared cases. Evidence marked *Recorded test* was prepared in advance and is not executed by this app.
- **Live AI:** click *Switch to Live AI*, edit Python code, expected and observed behaviour, then *Analyse my code*.
- **Verification:** `ast.parse` checks Python syntax **without executing** the code. The AI's hypothesis and suggested tests are not independently verified.
- **Accept/Reject:** records a decision but does not change files.
- **Request re-analysis:** records the decision and, only in Live AI mode, sends user feedback plus previous diagnosis to the configured model. In recorded mode it records the request only.
- **Logs:** decisions are appended to `decisions.jsonl`; no code is intentionally written to this log. Clear it before sharing if notes contain private information.

## Tests

```powershell
python -m unittest discover -s tests -v
```

## Architecture

Browser HTML/JS -> Python `ThreadingHTTPServer` -> recorded JSON cases / optional provider API. Independent Python `ast.parse` syntax check. Local decisions JSONL. No execution sandbox is implemented.

## Development record and AI disclosure

- **v1:** recorded cases, labelled evidence, Accept/Reject/Retry decision log; 3 automated tests and browser interactions verified by developer.
- **v2:** optional provider-backed dynamic analysis, feedback-based re-analysis, editable input, independent syntax check, validation and additional tests. **Live AI was tested locally on 14 November 2026 using a Volcengine Ark-hosted model. Initial diagnosis and feedback-driven re-analysis were demonstrated. This does not establish the correctness of model-generated suggestions.**
- **AI assistance:** ChatGPT generated initial project code, v2 changes, test scaffolding and documentation. The student should inspect, run, evaluate, correct and disclose assistance and verification in the submitted report. Do not claim empirical user-study results from demonstration cases.

## Limitations

No sandboxed code execution; no validation that model's suggested fix works; provider may return malformed JSON or errors; prompts are sent to the configured external provider; recorded cases do not establish novice learning effectiveness.
