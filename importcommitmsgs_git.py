from github import Github

def get_commit_messages(username, repository_name, token):
    # Create a GitHub instance using your personal access token
    g = Github(token)

    try:
        # Get the specified repository
        repo = g.get_repo(f"{username}/{repository_name}")

        # Get the default branch (usually 'master' or 'main')
        default_branch = repo.default_branch

        # Get the default branch's commit
        commit = repo.get_commit(sha=default_branch)

        # Extract commit messages
        commit_messages = [commit.commit.message for commit in repo.get_commits(sha=default_branch)]

        return commit_messages

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Replace these values with your GitHub username, repository name, and personal access token
github_username = "slackapi"
repository_name = "python-slack-sdk"
github_token = "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"

commit_messages = get_commit_messages(github_username, repository_name, github_token)

if commit_messages:
    print("Commit Messages:")
    for idx, message in enumerate(commit_messages, start=1):
        print(f"{idx}. {message}")
else:
    print("Failed to fetch commit messages.")
i