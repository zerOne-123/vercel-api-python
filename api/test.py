from flask import Flask, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
def test(path):
  name = request.args.get('name', 'pyf')
  return 'Hello ' + name