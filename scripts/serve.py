#!/bin/python

import http.server
import socketserver
import argparse


parser = argparse.ArgumentParser(description="Generate website pages.")
parser.add_argument("--port", type=int, default=8080, help="port to serve")
parser.add_argument("--dir", default="_site", help="dir to serve")

args = parser.parse_args()

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, directory=args.dir, **kwargs)

with socketserver.TCPServer(("", args.port), Handler) as httpd:
    try:
        print("Serving at port", args.port)
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
