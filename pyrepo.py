import os
import subprocess
from github import Github
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Github access token from the environment variable
access_token = os.getenv("GITHUB_ACCESS_TOKEN")

# Create a Github instance using the access token
g = Github(access_token)

# Ask the user for the location to create the Git repository
repo_location = input("Enter the location to create the Git repository: ")

# Ask the user for the name of the repository
repo_name = input("Enter the name of the repository: ")

# Create a new repository on GitHub
repo = g.get_user().create_repo(repo_name)

# Create a new directory for the repository
os.mkdir(os.path.join(repo_location, repo_name))

print("Github repository created")

# Initialize a new Git repository
subprocess.run(["git", "init"], cwd=os.path.join(repo_location, repo_name))

print("Git repository created.")


# Create a README file
with open(os.path.join(repo_location, repo_name, "README.md"), "w") as f:
    f.write("# " + repo_name)

# Create a .gitignore file
import requests

url = 'https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore'
response = requests.get(url)

with open(os.path.join(repo_location, repo_name, '.gitignore'), 'w') as f:
    f.write(response.text)
    f.write("*.wpr")

# Add the README and .gitignore files to the staging area
subprocess.run(["git", "add", "README.md", ".gitignore"], cwd=os.path.join(repo_location, repo_name))

# Commit the changes
subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=os.path.join(repo_location, repo_name))

# Add a remote named origin with the URL of the created repository using HTTPS
subprocess.run(["git", "remote", "add", "origin", f"https://github.com/Betawarrior12/{repo_name}.git"], cwd=os.path.join(repo_location, repo_name))

# Push to the main branch
subprocess.run(["git", "push", "-u", "origin", "main"], cwd=os.path.join(repo_location, repo_name))

print("Done.")
