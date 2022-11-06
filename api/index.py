from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world'


@app.route('/test')
def test():
    return 'Test'