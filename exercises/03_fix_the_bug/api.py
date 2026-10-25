# A tiny web API that uses the functions from bugs.py.
# Run it:
#   python exercises\03_fix_the_bug\api.py
# Then open these in your browser:
#   http://localhost:8000/count_to?n=5
#   http://localhost:8000/can_vote?age=18
#   http://localhost:8000/add_typed?a=5&b=3
#   http://localhost:8000/greeting?hour=9
# Press Ctrl+C in the terminal to stop it.
#
# Until you fix bugs.py, some of these give wrong answers. Fix the bugs,
# restart the API, and watch the answers change.

import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).parent))
import bugs


# Each route reads values from the URL (they always arrive as text)
# and calls one function from bugs.py.
ROUTES = {
    "/count_to": lambda q: bugs.count_to(int(q["n"])),
    "/can_vote": lambda q: bugs.can_vote(int(q["age"])),
    "/add_typed": lambda q: bugs.add_typed(q["a"], q["b"]),
    "/greeting": lambda q: bugs.greeting(int(q["hour"])),
}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        # parse_qs gives {"a": ["5"]}, so take the first value of each
        query = {key: values[0] for key, values in parse_qs(url.query).items()}

        if url.path not in ROUTES:
            self.send_json(404, {"error": "unknown path", "try": list(ROUTES)})
            return

        try:
            answer = ROUTES[url.path](query)
        except KeyError as e:
            self.send_json(400, {"error": f"missing value {e}"})
            return
        except ValueError:
            self.send_json(400, {"error": "that value needs to be a number"})
            return

        self.send_json(200, {"answer": answer})

    def send_json(self, status, data):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


print("API running at http://localhost:8000  (Ctrl+C to stop)")
try:
    HTTPServer(("localhost", 8000), Handler).serve_forever()
except KeyboardInterrupt:
    print("\nStopped.")
