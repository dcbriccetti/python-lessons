from random import choice
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class RequestHandler(SimpleHTTPRequestHandler):

    def write(self, s):
        self.wfile.write(bytes(s, "utf-8"))

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            user_agent = self.headers.get('User-Agent')
            messages = ('Have a nice day', 'So long', 'Come again soon')
            self.write("""
Hello person from %s.
Your user agent is %s.
%s.
""" % (self.client_address[0], user_agent or "unknown", choice(messages)))
            return
        
        SimpleHTTPRequestHandler.do_GET(self)
    
httpd = TCPServer(("", 8080), RequestHandler)
httpd.serve_forever()