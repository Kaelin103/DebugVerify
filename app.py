"""DebugVerify v2 local web app. User code is never executed."""
import json
import os
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock
from urllib.parse import urlsplit
from model import get_case, list_cases, diagnose, static_check, CASES

BASE = Path(__file__).resolve().parent
LOG = BASE / 'decisions.jsonl'
LOCK = Lock()
MAX_BYTES = 30000

def validate_analysis(body):
    if not isinstance(body, dict):
        raise ValueError('JSON object required')
    code, expected, observed = (body.get(k, '') for k in ('code', 'expected', 'observed'))
    feedback = body.get('feedback', '')
    previous = body.get('previous')
    if not all(isinstance(x, str) for x in (code, expected, observed, feedback)):
        raise ValueError('Inputs must be strings')
    if not code.strip() or len(code) > 12000 or len(expected) > 2000 or len(observed) > 2000 or len(feedback) > 2000:
        raise ValueError('Missing code or input exceeds length limit')
    if previous is not None and (not isinstance(previous, str) or len(previous) > 12000):
        raise ValueError('Invalid previous diagnosis')
    return code, expected, observed, feedback, previous

class Handler(BaseHTTPRequestHandler):
    def send_json(self, data, status=200):
        raw = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(raw)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        path = urlsplit(self.path).path
        if path == '/':
            raw = (BASE / 'index.html').read_bytes()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)
        elif path == '/api/cases':
            self.send_json({'cases': list_cases(), 'mode': 'recorded + optional live AI'})
        elif path.startswith('/api/cases/'):
            try:
                self.send_json(get_case(path.split('/')[-1]))
            except ValueError:
                self.send_json({'error': 'Unknown case'}, 404)
        elif path == '/api/health':
            self.send_json({'status': 'ok', 'live_ai_configured': bool(all(os.getenv(k) for k in ('DEBUGVERIFY_API_KEY', 'DEBUGVERIFY_MODEL', 'DEBUGVERIFY_API_URL'))), 'code_execution': False})
        elif path == '/favicon.ico':
            self.send_response(204)
            self.end_headers()
        else:
            self.send_json({'error': 'Not found'}, 404)

    def read_body(self):
        try:
            size = int(self.headers.get('Content-Length', '0'))
        except ValueError:
            raise ValueError('Invalid Content-Length')
        if not 0 < size <= MAX_BYTES:
            raise ValueError('Invalid request size')
        try:
            return json.loads(self.rfile.read(size))
        except (UnicodeDecodeError, json.JSONDecodeError):
            raise ValueError('Invalid JSON request')

    def do_POST(self):
        path = urlsplit(self.path).path
        if path not in ('/api/decision', '/api/analyse'):
            return self.send_json({'error': 'Not found'}, 404)
        try:
            body = self.read_body()
            if not isinstance(body, dict):
                raise ValueError('JSON object required')
            if path == '/api/analyse':
                code, expected, observed, feedback, previous = validate_analysis(body)
                check = static_check(code)
                result = diagnose(code, expected, observed, feedback, previous)
                return self.send_json({'mode': 'live AI', 'diagnosis': result, 'static_check': check,
                                       'notice': 'AI output is unverified. No user code was executed.'})
            case_id, choice = body.get('case_id'), body.get('choice')
            if case_id not in (*CASES, 'custom') or choice not in ('accept', 'reject', 'retry'):
                raise ValueError('Invalid case or choice')
            note = body.get('note', '')
            if not isinstance(note, str) or len(note) > 500:
                raise ValueError('Note must be at most 500 characters')
            record = {'time': datetime.now(timezone.utc).isoformat(), 'case_id': case_id,
                      'choice': choice, 'note': note}
            with LOCK:
                with LOG.open('a', encoding='utf-8') as file:
                    file.write(json.dumps(record, ensure_ascii=False) + '\n')
            return self.send_json({'status': 'recorded', 'record': record})
        except ValueError as exc:
            return self.send_json({'error': str(exc)}, 400)
        except Exception:
            return self.send_json({'error': 'Unexpected server error; see server logs.'}, 500)

if __name__ == '__main__':
    server = ThreadingHTTPServer(('127.0.0.1', 8000), Handler)
    print('DebugVerify v2 at http://127.0.0.1:8000', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping server')
    finally:
        server.server_close()
