from sanic import Sanic, response
from sanic.response import HTTPResponse, text
from sanic.request import Request

app = Sanic('a')

@app.get("/")
@app.route('/<path:path>')
async def index(request: Request, path='') -> HTTPResponse:
    # return text("Done.")
    return response.text('hello sanic.')