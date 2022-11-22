from sanic import Sanic
from sanic.response import json
app = Sanic("data")


@app.route('/<path:path>')
async def data(request, path=""):
    return json({'hello': path})