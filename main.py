from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse

class RequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    parsed_path = urlparse.urlparse(self.path)
    query_params = urlparse.parse_qs(parsed_path.query)

    name = query_params.get('name', ['Recruto'])[0]
    message = query_params.get('message', ['Давай дружить'])[0]

    response = f"Hello {name}! {message}!"

    self.send_response(200)
    self.send_header("Content-type", "text/html; charset=utf-8")
    self.end_headers()

    self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  print(f"Starting httpd server on port {port}")
  httpd.serve_forever()

if __name__ == "__main__":
  run()