port = 8080

from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import os

def load(path):
    file_path = os.path.join(os.path.dirname(sys.argv[0]), path)
    with open(file_path, 'rb') as f:  # Open the file in binary mode
        return f.read()  # Return the file content as bytes

# Define the request handler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # Handle GET requests
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(load("render/render.html"))
       
# Set up and start the HTTP server
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=1111):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":

    run(port=port)
