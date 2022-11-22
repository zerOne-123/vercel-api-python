from fastapi import FastAPI

app = FastAPI()


@app.route(__name__)
def main():
    return {
        "message": "Hello my friend",
        'a': __name__
    }
