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
        print(response.json())

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))

        # https://notify-bot.line.me/oauth/token?client_secret=A4vmKub5z4Ssf2tQA25B7GBXrZN7jND3EJiOgwjApMo
        # access_token

        # https://notify-bot.line.me/oauth/authorize?response_type=code&scope=notify&response_mode=form_post&state=%E7%B9%BC%E8%80%80&client_id=YaGCpDUilyJVMV4FvvppWm&redirect_uri=https://test-notify-xi.vercel.app/api