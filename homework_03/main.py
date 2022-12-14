from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello!"}


@app.get("/ping")
def ping():
    return {
        "message": "pong"
    }
