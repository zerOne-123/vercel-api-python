from fastapi import FastAPI

app = FastAPI()


@app.route('/api/fastapi')
def main():
    return {
        "message": "Hello my friend",
        'a': __name__
    }
