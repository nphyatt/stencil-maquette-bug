#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        if self.path.endswith('.js') or self.path.endswith('.js/') or self.path.endswith('.js.map') or self.path.endswith('.js.map/'):
            SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.send_response(302)
            self.send_header('Location', self.path + '.js')
            self.end_headers()


if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 4444)
