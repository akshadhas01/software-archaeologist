import requests
import base64


def get_repo(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    return response.json()


def get_languages(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    response = requests.get(url)
    return response.json()


def get_readme(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    response = requests.get(url)

    data = response.json()

    content = base64.b64decode(
        data["content"]
    ).decode("utf-8")

    return content[:5000]