import http.server
import socketserver
from random import randint

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def write(self, s): self.wfile.write(bytes(s, "utf-8"))
    def do_GET(self):
        print(self.path)
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.write("""
<html>
    <body>
        Your random number is %d
    </body>
</html>""" % randint(1, 100))
            return
        
        http.server.SimpleHTTPRequestHandler.do_GET(self)
    
httpd = socketserver.TCPServer(("", 8000), RequestHandler)
httpd.serve_forever()
