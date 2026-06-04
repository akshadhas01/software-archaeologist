from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "Software Archaeologist",
        "status": "running"
    }