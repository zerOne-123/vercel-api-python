from sanic import Sanic
from sanic.response import redirect, text

app = Sanic('vercel-sanic-test')


@app.route('/')
async def index(request):
    return redirect('https://vercel.com/')


@app.route('/ping')
async def pong(request):
    return text('pong!')

if __name__ == '__main__':
    app.run(auto_reload=True, port=8000)
