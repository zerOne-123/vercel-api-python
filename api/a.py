from sanic import Sanic
from sanic.response import HTTPResponse, text
from sanic.request import Request

app = Sanic('api')


@app.route('/<path:path>')
async def index(request: Request, path='') -> HTTPResponse:
    return text("Done.")
