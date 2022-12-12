# simple http server to serve the tiles organized in a directory structure
# based on the tile coordinates
# usage: python main.py
# then open http://localhost:PORT/ in your browser
# the tiles are expected to be in the directory structure
# /tiles/zoom/x/y.png

import http.server
import threading


PORT = 9000

# simple multithreaded http server
class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

server = http.server.HTTPServer(('', PORT), HttpRequestHandler)

server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()