from fastapi import FastAPI

app = FastAPI()


@app.get("/api/fastapi")
def main():
    return {
        "message": "Hello my friend",
        "a": __name__
    }
