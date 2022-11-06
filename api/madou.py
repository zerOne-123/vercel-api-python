from flask import Flask, request, Response, make_response
import requests
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    key = 'pnhXgN0U'
    iv = 'GY4gEvBD'
    url = request.args.get("url")
    
    if url == '':
        return ""
    
    img = requests.get(url).content
    # des = DES.new(key=key.encode(), mode=DES.MODE_CBC, iv=iv.encode())
    # return des.decrypt(pad(img, 16, style='pkcs7'))
    return img