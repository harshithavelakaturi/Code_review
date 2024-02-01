import requests
from textblob import TextBlob

def get_commit_messages(owner, repo, pull_number):
    # Make a request to the GitHub API to get pull request data
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/commits'
    response = requests.get(url)
    data = response.json()

    # Extract commit messages
    commit_messages = [commit['commit']['message'] for commit in data]

    return commit_messages

def analyze_sentiment(commit_messages):
    # Perform sentiment analysis using TextBlob
    sentiments = [TextBlob(message).sentiment.polarity for message in commit_messages]

    return sentiments

# Example usage
owner = 'TheAlgorithms'
repo = 'Java'
pull_number = 1  # Replace with the desired pull request number

commit_messages = get_commit_messages(owner, repo, pull_number)
sentiments = analyze_sentiment(commit_messages)

# Print commit messages and their sentiments
for message, sentiment in zip(commit_messages, sentiments):
    print(f"Commit Message: {message}")
    print(f"Sentiment: {sentiment}\n")
