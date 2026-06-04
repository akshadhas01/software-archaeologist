from fastapi import FastAPI
from github_service import (
    get_repo,
    get_languages,
    get_readme
)

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


@app.get("/languages/{owner}/{repo}")
def languages(owner: str, repo: str):
    return get_languages(owner, repo)


@app.get("/readme/{owner}/{repo}")
def readme(owner: str, repo: str):
    return {
        "readme": get_readme(owner, repo)
    }