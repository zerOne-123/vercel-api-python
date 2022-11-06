from sanic import Sanic
from sanic.response import json
app = Sanic(name="myApp")

@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
  # print(request)
  return json({'hello': path})