import http.server
import socketserver
import os
import sys

PORT = 3000
DEFAULT_FILE = 'dist.html'

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = f'/{DEFAULT_FILE}'

        # Check if DEFAULT_FILE exists in the current directory or create it if it doesn't
        if not os.path.isfile(DEFAULT_FILE):
            with open(DEFAULT_FILE, 'w') as file:
                file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Default Page</title>\n</head>\n<body>\n<h1>This is a default page.</h1>\n</body>\n</html>\n")
            print(f"Created '{DEFAULT_FILE}' with default content.")

        # Serve the request
        return super().do_GET()

def run_server():
    try:
        # Change directory to where the script is located to ensure correct file serving
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print(f"Serving on port {PORT}")
            httpd.serve_forever()
    except OSError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)

if __name__ == "__main__":
    run_server()
