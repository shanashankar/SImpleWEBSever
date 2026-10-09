from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
<title>Laptop Specifications</title>
</head>
<body>


<p><strong>Name:</strong>Sahana shankar</p>
<p><strong>Register Number:</strong>26002875</p>




</body>
</html>
"""


class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header("content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode())


server_address = ("", 8000)

httpd = HTTPServer(server_address, myhandler)

print("my webserver is running...")

httpd.serve_forever()