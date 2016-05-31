# Run this, then in your web browser, go to http://localhost:8080/quote or http://localhost:8080/joke

from http.server import HTTPServer, SimpleHTTPRequestHandler
from random import choice

quotes = (
    'Computer science is no more about computers than astronomy is about telescopes. - Edsger Dijkstra',
    'People think that computer science is the art of geniuses but the actual reality is the opposite, ' +
        'just many people doing things that build on each other, like a wall of mini stones. - Donald Knuth',
    'Programs must be written for people to read, and only incidentally for machines to execute. - H. Abelson and G. Sussman',
    "I don't know how many of you have ever met Dijkstra, but you probably know that arrogance in computer science is measured in nano-Dijkstras. - Alan Kay"
)

jokes = (
    'Why did the chicken cross the road? To get to the other side.',
)

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        category = quotes if self.path == '/quote' else jokes
        html = """
<html>
    <body>
        <h1 style='font-family: sans-serif; color: darkblue;'>%s</h1>
    </body>
</html>
            """ % choice(category)
        self.wfile.write(html.encode("utf-8"))

server = HTTPServer(('', 8080), Handler)
server.serve_forever()
