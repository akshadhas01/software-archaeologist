from fastapi import FastAPI
from github_service import get_repo

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "Software Archaeologist",
        "status": "running"
    }

@app.get("/repo/{owner}/{repo}")
def repo_info(owner: str, repo: str):

    data = get_repo(owner, repo)

    return {
        "name": data["name"],
        "description": data["description"],
        "stars": data["stargazers_count"],
        "language": data["language"]
    }