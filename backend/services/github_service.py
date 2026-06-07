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

    return content[:3000]


def get_health_score(owner, repo):

    repo_data = get_repo(owner, repo)

    score = 50

    if repo_data["stargazers_count"] > 1000:
        score += 20

    if repo_data["forks_count"] > 100:
        score += 10

    if repo_data["open_issues_count"] < 100:
        score += 20

    return min(score, 100)


def get_contributors(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"

    response = requests.get(url)

    return response.json()


def build_summary(owner, repo):

    repo_data = get_repo(owner, repo)

    languages = get_languages(owner, repo)

    return {
        "repository": repo_data["name"],
        "description": repo_data["description"],
        "stars": repo_data["stargazers_count"],
        "forks": repo_data["forks_count"],
        "health_score": get_health_score(owner, repo),
        "top_languages": list(languages.keys())[:5]
    }


def build_report(owner, repo):

    repo_data = get_repo(owner, repo)
    languages = get_languages(owner, repo)

    stars = repo_data["stargazers_count"]

    top_language = (
        list(languages.keys())[0]
        if languages
        else "Unknown"
    )

    if stars > 100000:
        community_size = "Very Large"
    elif stars > 10000:
        community_size = "Large"
    else:
        community_size = "Growing"

    if len(languages) >= 5:
        difficulty = "Advanced"
    elif len(languages) >= 3:
        difficulty = "Intermediate"
    else:
        difficulty = "Beginner Friendly"

    return {
        "difficulty": difficulty,
        "community_size": community_size,
        "top_language": top_language,
        "recommended_starting_point": "README.md",
        "repository_type": "Open Source Project"
    }