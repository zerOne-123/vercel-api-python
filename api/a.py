from sanic import Sanic
from sanic.response import text

app = Sanic('vercel-api-python')


@app.route('/<path:path>')
async def index(request, path=""):
    return text("Hello, world.")
