from flask import Flask, request

app = Flask(__name__)

@app.route('/<path:path>')
def test5():
  name = request.args.get('name', 'py')
  return 'Hello a b ' + name