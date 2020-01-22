#!/usr/bin/python3

from sys import argv
from subprocess import Popen, PIPE
from wsgiref.simple_server import make_server

process = Popen(argv[1:], stdin=PIPE, stdout=PIPE)

def app(env, response):
    response('200 OK', [('Content-type', 'text/plain; charset=utf-8')])

    process.stdin.write(env['QUERY_STRING'].encode())
    process.stdin.write(b"\n")
    process.stdin.flush()
    body = process.stdout.readline()

    return [body]

with make_server('', 8000, app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
