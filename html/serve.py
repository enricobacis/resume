#!/usr/bin/env python2

from SimpleHTTPServer import SimpleHTTPRequestHandler
from SocketServer import TCPServer
from webbrowser import open_new
from threading import Timer

HOST = '127.0.0.1'
PORT = 8000
PAGE = 'index.html'

Timer(1.0, open_new, args=['%s:%d/%s' % (HOST, PORT, PAGE)]).start()

server = TCPServer((HOST, PORT), SimpleHTTPRequestHandler)
server.allow_reuse_address = True
server.serve_forever()
