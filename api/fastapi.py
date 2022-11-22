from fastapi import FastAPI

app = FastAPI()


@app.get('/'+__name__)
async def root():
    return {"message": "Hello World"}
