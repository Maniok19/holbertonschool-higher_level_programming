#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from task_03_http_server import MyHandler
import json

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
