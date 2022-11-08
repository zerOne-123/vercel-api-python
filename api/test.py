from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def test1():
  name = request.args.get('name', 'py')
  return '/ ' + name

@app.route('/api/test')
def test2():
  name = request.args.get('name', 'py')
  return '/api/test ' + name

@app.route('/api/b')
def test5():
  name = request.args.get('name', 'py')
  return '/api/b ' + name

@app.route('/api')
def test5():
  name = request.args.get('name', 'py')
  return '/api ' + name

@app.route('/api/test/mm')
def test3():
  name = request.args.get('name', 'py')
  return '/api/test/mm ' + name

@app.route('/api/test/m')
def test4():
  name = request.args.get('name', 'py')
  return '/api/test/m ' + name

@app.route('/<path:path>')
def test5(path):
  name = request.args.get('name', 'py')
  return 'Hello ' + name