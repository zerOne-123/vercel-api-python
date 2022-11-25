from sanic import Sanic
from sanic.response import json
app = Sanic('api')


@app.get('/<path:path>')
async def index(request, path=""):
    return json({'hello': path})
