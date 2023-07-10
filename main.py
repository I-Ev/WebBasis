from http.server import BaseHTTPRequestHandler, HTTPServer

host = 'localhost'
port = 8000

class Myserver(BaseHTTPRequestHandler):


    def do_GET(self):
        with open('./index4.html', encoding='utf-8') as file:
            html_content = file.read()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # HTML content for the "Contacts" page
        content = html_content

        self.wfile.write(content.encode())


def main():

    server_address = (host, port)

    httpd = HTTPServer(server_address, Myserver)
    print(f"Starting server on {host}:{port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass
    httpd.server_close()
    print("Server stopped.")



if __name__ == '__main__':
    main()
