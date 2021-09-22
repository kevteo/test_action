##
##from github import Github
##import os
##from pprint import pprint
##
### token = os.getenv('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', '...')
##g = Github(os.environ.get('GIT_PAT', 'a'))
##repo = g.get_repo("kevteo/test_action")
##
##print(repo)
##
##def push(path, message, content, branch, update=False):
##    author = InputGitAuthor(
##        "ai-sdk",
##        "noreply.ai-sdk@gmail.com"
##    )
##    source = repo.get_branch("master")
##    repo.create_git_ref(ref=f"refs/heads/{branch}", sha=source.commit.sha)  # Create new branch from master
##    if update:  # If file already exists, update it
##        contents = repo.get_contents(path, ref=branch)  # Retrieve old file to get its SHA and path
##        repo.update_file(contents.path, message, content, contents.sha, branch=branch, author=author)  # Add, commit and push branch
##    else:  # If file doesn't exist, create it
##        repo.create_file(path, message, content, branch=branch, author=author)  # Add, commit and push branch
##
##
##
##file_path = "requirements.txt"
##push(file_path, "Add pytest to dependencies.", data, "update-dependencies", update=True)
##


import json

with open('data.json') as f:
    json1 = json.load(f)
