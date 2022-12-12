# simple http server to serve the tiles organized in a directory structure
# based on the tile coordinates
# usage: python main.py
# then open http://localhost:PORT/ in your browser
# the tiles are expected to be in the directory structure
# /tiles/zoom/x/y.png

import http.server
import socketserver

PORT = 9000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
