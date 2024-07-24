from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import parse_qs
import requests

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

        code = data['code'][0]
        state = data['state'][0]

        url = 'https://notify-bot.line.me/oauth/token'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        parameters = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'https://test-notify-xi.vercel.app/api',
            'client_id': 'YaGCpDUilyJVMV4FvvppWm',
            'client_secret': 'A4vmKub5z4Ssf2tQA25B7GBXrZN7jND3EJiOgwjApMo'
        }

        response = requests.post(url, headers=headers, params=parameters)
        if response.status_code != 200:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response.json(), ensure_ascii=False).encode('utf-8'))
            return
        access_token = response.json()['access_token']

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({
            'state': state,
            'access_token': access_token
        }, ensure_ascii=False).encode('utf-8'))
