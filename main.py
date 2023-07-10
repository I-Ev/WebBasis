from http.server import BaseHTTPRequestHandler, HTTPServer

host = 'localhost'
port = 8000

class Myserver(BaseHTTPRequestHandler):

    def __get_content(self):
        return """
        <!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
</head>
<body>
<div class="container text-center">
    <div class="row">
        <div class="col-sm-3">

            <nav class="navbar bg-dark border-bottom border-bottom-dark" data-bs-theme="dark">
                <div class="col-2">
                    <img src="https://ajanuw.gallerycdn.vsassets.io/extensions/ajanuw/bs5/0.7.0/1646364353922/Microsoft.VisualStudio.Services.Icons.Default"
                         alt="Bootstrap" width="30" height="24">
                </div>
                <div class="col-10">
                    <div class="container text-center">

                        <p class="text-white bg-dark">Меню</p>
                    </div>
                </div>

                </a>
                <hr width="500px;"
                    color="white"
                    size="4"
                    align="center">
            </nav>
            <ul class="nav flex-column">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Active</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Link</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Link</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link">Disabled</a>
                </li>
            </ul>
        </div>
        <div class="col-sm-9 mt-5">
            <div class="container text-center">
                <h1>Контакты</h1>
                <div class="row">
                    <div class="col-5">
                        <div class="card-body">
                            <div class="input-group mb-3">
                                <label class="form-label">First name</label>
                                <br>
                                <span class="input-group-text" id="basic-addon1">@</span>
                                <input type="text" class="form-control" placeholder="Username" aria-label="Username"
                                       aria-describedby="basic-addon1">
                            </div>

                            <div class="input-group mb-3">
                                <input type="text" class="form-control" placeholder="Recipient's username"
                                       aria-label="Recipient's username" aria-describedby="basic-addon2">
                                <span class="input-group-text" id="basic-addon2">@example.com</span>
                            </div>

                            <div class="input-group">
                                <span class="input-group-text">With textarea</span>
                                <textarea class="form-control" aria-label="With textarea"></textarea>
                            </div>
                        </div>
                    </div>
                    <div class="col-5">
                        <div class="container text-center">
                            <h6 align="left">Наши контакты</h6>
                            <dd align="left">A description list is perfect for defining terms Align terms and
                                descriptions horizontally by using our grid system’s predefined classes (or semantic
                                mixins). For longer terms, you can optionally add.
                            </dd>

                        </div>


                    </div>


                </div>
            </div>

</body>
</html>
        """

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # HTML content for the "Contacts" page
        content = self.__get_content()

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
