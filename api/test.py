from sanic import Sanic
from sanic.response import json
app = Sanic(name='api')

@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
  # print(request)
  return json({'hello': path})