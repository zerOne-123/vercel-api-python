from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def test():
  name = request.args.get('name', 'py')
  return '/ ' + name

@app.route('/api/test')
def test():
  name = request.args.get('name', 'py')
  return '/api/test ' + name

@app.route('/api/test/mm')
def test():
  name = request.args.get('name', 'py')
  return '/api/test/mm ' + name

@app.route('/api/test/m')
def test():
  name = request.args.get('name', 'py')
  return '/api/test/m ' + name

@app.route('/<path:path>')
def test(path):
  name = request.args.get('name', 'py')
  return 'Hello ' + name