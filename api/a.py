from sanic import Sanic, response
from sanic.response import HTTPResponse, text
from sanic.request import Request

app = Sanic('api')

@app.get("/")
@app.route('/<path:path>')
async def index(request: Request, path='') -> HTTPResponse:
    # return text("Done.")
    print(path)
    return response.text('hello sanic.')