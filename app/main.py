from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello from FastAPI + GitHub Actions + Docker on EC2!"}


@app.get("/ping")
def ping():
    return {"status": "ok", "ping": "pong"}
