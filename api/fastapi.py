from fastapi import FastAPI

app = FastAPI()


@app.route('/<path:path>')
def main():
    return {
        "message": "Hello my friend"
    }
