from fastapi import FastAPI

app = FastAPI()


@app.get("/api/fastapi")
async def root():
    return {"message": "Hello World"}
