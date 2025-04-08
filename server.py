from http.server import SimpleHTTPRequestHandler, HTTPServer
import subprocess

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/run-script":
            result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(result.stdout.encode())
        else:
            super().do_GET()

PORT = 5500
server = HTTPServer(("localhost", PORT), RequestHandler)
print(f"Server running on http://localhost:{PORT}")
server.serve_forever()
