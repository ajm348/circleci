import os
import http.server

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000)) # Use PORT if it’s there.
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, http.server.CGIHTTPRequestHandler)
    httpd.serve_forever()
