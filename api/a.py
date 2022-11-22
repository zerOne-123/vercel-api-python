from sanic import Sanic, response
from sanic.response import HTTPResponse, text
from sanic.request import Request

app = Sanic('api')

@app.get("/")
@app.route('/<path:path>')
async def index(request: Request, path='') -> HTTPResponse:
    # return text("Done.")
    return response.text('hello sanic.')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888)