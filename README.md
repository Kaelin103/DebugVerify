# DebugVerify v2 — IIS Assignment 2

**README prose word count:** 673 (excluding code blocks)

## Project Status

DebugVerify is a local interactive prototype designed to help novice programmers critically evaluate AI-generated debugging suggestions rather than accept them automatically.

The prototype provides two modes:

- **Recorded Mode (implemented, pre-authored content):** Three repeatable cases demonstrate a useful suggestion, misleading advice and an uncertain diagnosis. Recorded tests are prepared in advance, not executed by the application.
- **Live AI Mode (implemented and locally tested):** Users submit Python code, expected and observed behaviour, and optional feedback to an external language model for diagnosis and re-analysis.

Both modes support a four-stage interaction: Problem Context, Diagnosis, Verification Evidence and Your Decision.

The prototype does not execute user-submitted code, automatically modify files or guarantee that AI-generated suggestions are correct.

## Technology Stack

- **Frontend:** HTML and JavaScript (`index.html`).
- **Backend:** Python standard-library `ThreadingHTTPServer` (`app.py`).
- **Analysis:** Recorded JSON cases or an external OpenAI-compatible chat-completions API (`model.py`).
- **Independent check:** Python `ast.parse()` for syntax checking only.
- **Decision logging:** Local `decisions.jsonl`, excluded from Git.
- **Test framework:** Python `unittest`.

Live AI testing used a Volcengine Ark-hosted model on 14 November 2026. The model is an external service, not a locally trained model.

## Running the Prototype

Install Python 3 and Git, then open Windows PowerShell:

```powershell
git clone https://github.com/Kaelin103/DebugVerify.git
cd DebugVerify
python app.py
```

Open `http://127.0.0.1:8000` in a browser. Stop the server with `Ctrl+C`.

Recorded Mode requires no API key. No additional Python packages are required for the standard-library implementation.

### Optional Live AI Configuration

Set `DEBUGVERIFY_API_URL`, `DEBUGVERIFY_MODEL` and `DEBUGVERIFY_API_KEY` in the terminal before starting the server.

The endpoint must support the expected chat-completions request and response format. Compatibility depends on the provider.

Enter the API key without displaying it on screen:

```powershell
$env:DEBUGVERIFY_API_URL = "https://YOUR_PROVIDER/v1/chat/completions"
$env:DEBUGVERIFY_MODEL = "YOUR_MODEL_ID"
$secureKey = Read-Host "API key" -AsSecureString
$ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureKey)
try {
    $env:DEBUGVERIFY_API_KEY = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($ptr)
}
finally {
    [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr)
}
python app.py
```

The application requires a plaintext environment variable at runtime. Do not commit keys, store them in source files or include them in screenshots. Avoid sending sensitive code to external AI providers.

## Interaction and Limitations

Users inspect the suggested diagnosis and supporting information before selecting **Accept**, **Reject** or **Request re-analysis**.

In Live AI Mode, the independent AST check establishes only whether Python syntax can be parsed. It does not execute user code or verify the program's behaviour or the AI's proposed fix.

Accept, Reject and Retry are recorded locally without modifying source code. In Recorded Mode, Retry only records the request. In Live AI Mode, the browser also sends feedback and the previous diagnosis to /api/analyse to request another model response. The decision log does not trigger re-analysis.

Decision records are stored locally in `decisions.jsonl`.

## Testing and Evidence

Run the automated tests:

```powershell
python -m unittest discover -s tests -v
```

Seven automated tests passed during local validation.

Supporting material:

- [Automated test results](evidence/V2_AUTOMATED_TEST_RESULTS.txt)
- [Manual test record](evidence/TEST_RECORD.md)
- [Live AI screenshots](evidence/)
- [Revised system architecture](docs/storyboards/final/DebugVerify_Architecture_Revised.png)
- [Three interaction storyboards](docs/storyboards/final/STORYBOARDS.md)

The Live AI tests demonstrate initial diagnosis and feedback-driven re-analysis. They do not establish debugging accuracy or improved learning outcomes.

## Development Record

The project developed through two principal stages.

**v1:** Three recorded debugging cases, evidence labels, a four-stage interface and user decision logging.

**v2:** Editable Live AI inputs, external model integration, feedback-driven re-analysis, independent AST syntax checking, input validation and additional tests.

Development decisions, testing and revisions are documented in [DEVELOPMENT_LOG.md](docs/DEVELOPMENT_LOG.md).

The initial prototype was committed as `079cf1c`. The README and project documentation were updated in `e711f10`. The final corrected architecture diagram was committed as `453a0f3`. Further changes are available in the repository's commit history.

## AI Assistance and Validation

ChatGPT assisted with code generation, interface revisions, test scaffolding, documentation and design materials.

Generated material was reviewed against the intended interaction and tested locally. Validation included automated unit tests, browser interaction checks, recorded-case demonstrations, and a Live AI diagnosis followed by feedback-driven re-analysis.

The recorded cases are demonstrations, not empirical user-study results. AI-generated explanations remain unverified hypotheses unless supported by independent evidence.

## Additional Files

The `cases/` directory contains recorded scenarios. `tests/` contains automated tests. `evidence/` contains screenshots and validation records. `docs/` contains architecture and development materials.

No additional ZIP or video is required to inspect the repository.

## Remaining Limitations

DebugVerify has no execution sandbox, automatic patch verification or measured user-learning outcomes. External model responses can be incorrect or unavailable. Further evaluation with novice programmers would be required to assess whether the interaction improves debugging decisions.