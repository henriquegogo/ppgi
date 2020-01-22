# PPGI
Persistent Process Gateway Interface

## Why?
CGI is easy, but a new process for each request it's not good

## How?
Start a single process. Every request why send a stdin to it. Return to user printing in stdout.

## And FastCGI?
Yeah, I know that "multi process" problem was solved a long time ago with FastCGI and alternatives, but the thing it's don't touch in backends code/app to adapt to server. Just run and listen/respond to stdin and stdout

## Just for Python?
No. The server is implemented in Python but the application could be writed in any language. Just create a persistent process and listen to stdin.

## Example
```sh
./ppgi.py cat
```
This will print any QUERY_STRING to user.
