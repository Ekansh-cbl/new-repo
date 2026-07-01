from http.server import BaseHTTPRequestHandler, HTTPServer

PAGES = {
    "/": """<html><body><h1>DualCam Ops</h1><p>Preview health check</p></body></html>""",
    "/health": "{\"status\": \"ok\"}",
}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = PAGES.get(self.path, PAGES["/"])
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode())


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
