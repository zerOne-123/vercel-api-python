from flask import Flask

app = Flask(__name__)

@app.route('/<path:path>')
def catch_all(path):
    return 'hello flask'
