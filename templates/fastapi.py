from fastapi import FastAPI

app = FastAPI()

@app.get('/{path:path}')
async def root(path):
    return {"message": "Hello World", "path": path}
