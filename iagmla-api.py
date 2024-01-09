# Administer iamgla-api-org

from requests import post, get

def get_branch(
        username: str,
        account: str,
        repo : str,
        token : str,
        branch: str,
    ) -> str:
    base_uri = "https://api.github.com/repos/" + username + "/" + repo + "/git/refs/"
    headers = {
        'Accept': "application/vnd.github+json",
        'X-GitHub-Api-Version': '2022-11-28',
    }
    get_json = {"ref": branch, "access_token": token}
    req = get(base_uri, headers=headers, json=get_json)
    if req.status_code == 200:
        return req.text
    return ""

def create_branch(
        username: str,
        account: str,
        repo : str,
        branch : str,
        token : str,
        source_branch: str,
    ) -> bool:
    #base_uri = account + "/repos/" + username + "/git/refs/" + name
    base_uri = "https://api.github.com/repos/" + username + "/" + repo + "/git/refs"
    print(base_uri)
    headers = {
        'Accept': "application/vnd.github+json",
        'X-GitHub-Api-Version': '2022-11-28',
    }
    branch_ref = "refs/heads/" + branch
    post_json = {"ref": branch_ref, "access_token": token}
    req = post(
            base_uri,
            json = post_json,
            headers=headers
            )
    if req.status_code == 200:
        return True
    print(req.text)
    return False

f = open("github_access_token", "r")
token = f.read()
f.close()

username = "iagmla"
account = "https://api.github.com/repos/iagmla-api-org"
repo = "demo-repository"
main_branch = "main_branch"
new_branch = "test_branch"

branch_hash = get_branch(
    username=username,
    account=account,
    repo=repo,
    token=token,
    branch=main_branch)
print(branch_hash)
result = create_branch(
    username=username,
    account=account,
    repo=repo,
    branch=new_branch,
    token=token,
    source_branch=main_branch)
print(result)
