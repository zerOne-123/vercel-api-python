from flask import Flask, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def test(path):
  name = request.args.get('name', 'py')
  return 'Hello ' + name