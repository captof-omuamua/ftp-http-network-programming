from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class MyServer(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type='text/plain'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        resource_path = self.path.lstrip('/')
        if os.path.exists(resource_path):
            with open(resource_path, 'rb') as file:
                self._set_headers()
                self.wfile.write(file.read())
        else:
            self._set_headers(404, 'text/html')
            self.wfile.write(b'Resource not found')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        resource_path = self.path.lstrip('/')
        with open(resource_path, 'wb') as file:
            file.write(post_data)
        self._set_headers(201, 'text/html')
        self.wfile.write(b'Resource created')

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)
        resource_path = self.path.lstrip('/')
        with open(resource_path, 'wb') as file:
            file.write(put_data)
        self._set_headers(200, 'text/html')
        self.wfile.write(b'Resource updated')

    def do_DELETE(self):
        resource_path = self.path.lstrip('/')
        if os.path.exists(resource_path):
            os.remove(resource_path)
            self._set_headers(200, 'text/html')
            self.wfile.write(b'Resource deleted')
        else:
            self._set_headers(404, 'text/html')
            self.wfile.write(b'Resource not found')

def run_server(server_class=HTTPServer, handler_class=MyServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
