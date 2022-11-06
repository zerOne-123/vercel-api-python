from flask import Flask, request
from Crypto.Cipher import AES, DES
import requests
import base64

app = Flask(__name__)


@app.route('/')
def hello():
  return 'Hello, world'

@app.route('/test')
def test():
  return 'Test'

@app.route('/madou')
def madou():
  key = 'pnhXgN0U'
  iv = 'GY4gEvBD'
  url = request.args.get("url")

  img = requests.get(url).content
  des = DES.new(key=key.encode(), mode=DES.MODE_CBC, iv=iv.encode())
  return base64.b64decode(des.decrypt(base64.b64decode(img)).decode().replace('data:image/jpg;base64,', ''))
  # return img