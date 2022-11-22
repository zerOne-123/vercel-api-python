from sanic import Sanic, response
from sanic.response import HTTPResponse, text
from sanic.request import Request

app = Sanic('api')


@app.get("/")
@app.route('/<path:path>')
async def index(request: Request, path='') -> HTTPResponse:
    # return text("Done.")
    print(path)
    return text('hello sanic.')

if __name__ == '__main__':
    app.run(auto_reload=True, port=8000)
