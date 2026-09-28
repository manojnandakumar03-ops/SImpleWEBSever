from http.server import HTTPServer, BaseHTTPRequestHandler


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            name = "MANOJ N"
            ref_no = "26000161"

            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Home</title>
            </head>
            <body style="height:100vh; margin:0; display:flex; flex-direction:column;
                         justify-content:center; align-items:center; font-family:Arial;">
                <h1 style="color:#2a7de1;">Name: {name}</h1>
                <p style="color:#e14b2a; font-size:1.5rem;">Reference No: {ref_no}</p>
            </body>
            </html>
            """

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_error(404, "Page Not Found")


server = HTTPServer(("127.0.0.1", 8000), MyHandler)
print("Server is running at http://127.0.0.1:8000")
server.serve_forever()