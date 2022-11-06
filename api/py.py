from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def catch_all():
    return 'aaa'

# from http.server import BaseHTTPRequestHandler
 
 
# class handler(BaseHTTPRequestHandler):
 
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/plain')
#         self.end_headers()
#         self.wfile.write("DearXuan's API by python!".encode())
#         return