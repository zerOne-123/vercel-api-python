from flask import Flask, request
from Crypto.Cipher import AES, DES
import requests
import base64

app = Flask(__name__)

@app.route('/test')
def test():
  name = request.args.get('name', 'py')
  return 'Hello ' + name