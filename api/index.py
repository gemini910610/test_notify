from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import parse_qs

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(self.path.encode('utf-8'))
        return
    def do_POST(self):
        length = int(self.headers['content-length'])
        data = self.rfile.read(length)
        data = parse_qs(data.decode())

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))