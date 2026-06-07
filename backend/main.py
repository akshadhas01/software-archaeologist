from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.github_service import (
    get_repo,
    get_languages,
    get_readme,
    get_health_score,
    get_contributors,
    build_summary,
    build_report
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.get("/health/{owner}/{repo}")
def health(owner: str, repo: str):

    return {
        "health_score": get_health_score(owner, repo)
    }


@app.get("/contributors/{owner}/{repo}")
def contributors(owner: str, repo: str):

    data = get_contributors(owner, repo)

    return data[:10]


@app.get("/summary/{owner}/{repo}")
def summary(owner: str, repo: str):

    return build_summary(owner, repo)


@app.get("/report/{owner}/{repo}")
def report(owner: str, repo: str):

    return build_report(owner, repo)