# vercel-api-python

> 建议先通读下官方文档：<https://vercel.com/docs/concepts/functions/serverless-functions>

## 最简单例子

``` bash
├── api
|  ├── js.js
|  ├── py.py
```

| 文件扩展       | 语言    |
| :------------- | :------ |
| .js, .mjs, .ts | Node.js |
| .py            | Python  |
| .go            | Go      |
| .rb            | Ruby    |

```js
// api/js.js
export default function handler(req, res) {
  const { name = 'World' } = req.query;
  return res.send(`Hello ${name}!`);
}
```

```python
# api/py.py
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(b'Hello from Python from a Serverless Function!')
        return
```

# Node.js 最佳实践

> 文档：<https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/node-js>  
> nodejs api 文档：<https://nodejs.org/api/>

```bash
├── api
|  ├── js.js
└── package.json		  // 添加模块
└── package-lock.json	// 该文件通过 npm 命令添加模块会自动生成
```
```json
// package.json
{
  "dependencies": {
    "axios": "^1.1.3",		// 请求数据
    "crypto-js": "^4.1.1"	// 加解密
  }
}
```

> 可通过 npm 命令自己添加需要的包，查找官网：<https://www.npmjs.com/>


```js
// api/js.js
module.exports = (req, res) => {
  try {
    let who = req.query?.who || 'anonymous';
  	res.status(200).send(`Hello ${who}!`);
  } catch (error) {
    res.status(400).json({ error: 'My custom 400 error' });
  }
};
```

| 方法                         | 描述                                                         | 对象     |
| :--------------------------- | :----------------------------------------------------------- | :------- |
| `req.query`                  | 包含请求查询字符串的对象，如果如果请求没有查询字符串，则为 `{}` | Request  |
| `req.cookies`                | 包含请求发送的 Cookie 的对象，如果请求不包含 Cookie，则为 `{}` | Request  |
| `req.body`                   | 一个对象，包含请求发送的正文，如果未发送正文，则为 `null`    | Request  |
| `res.status(code)`           | 用于设置随响应发送的状态代码的函数，必须是有效的 HTTP 状态代码 | Response |
| `res.setHeader(name, value)` | 设置响应头函数                                               | Response |
| `res.send(body)`             | 设置响应内容函数，可以是 `body` `string` `object` `Buffer`   | Response |
| `res.json(obj)`              | 用于发送 JSON 响应的函数                                     | Response |

`req.body` 的值是是由请求头上的 `Content-type` 值决定的

| `Content-Type` 值                   | `req.body` 值          |
| :---------------------------------- | :--------------------- |
| 无                                  | `undefined`            |
| `application/json`                  | 随请求发送的 JSON 对象 |
| `application/x-www-form-urlencoded` | 随请求发送的表单数据   |
| `text/plain`                        | 随请求发送的文本字符串 |
| `application/octet-stream`          | 随请求发送的数据缓冲流 |

## Python 最佳实践

> 文档：<https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python>  
> Python 文档：<https://docs.python.org/zh-cn/3.9/index.html>

```bash
├── api
|  ├── base.py
|  ├── flask.py
|  ├── sanic.py
└── requirements.txt
```

```txt
// requirements.txt
Flask
sanic
requests
pycryptodome
```

> 可自己添加需要的模块包，查找官网：<https://pypi.org/>

```python
# api/base.py	无依赖服务器网关接口
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(b'Hello from Python from a Serverless Function!')
        return
```

```python
# api/flask.py	Web 服务器网关接口
from flask import Flask, Response
app = Flask(__name__)

@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
```

> flask 文档：<https://dormousehole.readthedocs.io/en/latest/>

```python
# api/sanic.py	异步服务器网关接口
from sanic import Sanic
from sanic.response import json
app = Sanic()

@app.route('/<path:path>')
async def index(request, path=""):
    return json({'hello': path})
```

> sanic 文档：https://sanic.dev/zh/