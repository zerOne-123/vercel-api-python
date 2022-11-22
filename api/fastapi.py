from fastapi import FastAPI

app = FastAPI()


@app.get('/<path:path>')
async def root():
    return {"message": "Hello World"}
