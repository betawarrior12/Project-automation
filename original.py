import os
import shutil
from subprocess import PIPE, run
import sys
from github import Github
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Github access token from the environment variable
access_token = os.getenv("GITHUB_ACCESS_TOKEN")

# Create a Github instance using the access token
g = Github(access_token)

def find_all_paths(source):
    path = None
    d = []
    
    for root, dirs, files in os.walk(source):
        for directory in dirs:
            d.append(directory)
        break

    for ind, i in enumerate(d):
        print(f"{ind}: {i}")

    dir_chosen = int(input("Enter index of template to be chosen: "))
    path = d[dir_chosen]

    return os.path.join(source, path)

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def copy_and_overwrite(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)



def main():
    source = "C:\\Users\\USER\\Pemi\\Python\\Templates"
    target = input("Enter taget path: ")
    path = find_all_paths(source)
    new_dir = "src"
    create_dir(target)

    dest_path = os.path.join(target, new_dir)
    copy_and_overwrite(path, dest_path)
    print("Done")
    print("Copied template to target dir")
    repo_create = input("Would you like to create a github repo for it. Y/N").upper()
    if repo_create == "Y":

        repo_location = dest_path
        # Ask the user for the name of the repository
        repo_name = input("Enter the name of the repository: ")
        # Create a new repository on GitHub
        repo = g.get_user().create_repo(repo_name)

        subprocess.run(["git", "init"], cwd=os.path.join(repo_location, repo_name))
        
        # Create a README file
        with open(os.path.join(repo_location, repo_name, "README.md"), "w") as f:
            f.write("# " + repo_name)
        
        # Create a .gitignore file
        with open(os.path.join(repo_location, repo_name, ".gitignore"), "w") as f:
            f.write("*.pyc\n__pycache__/\n")
        
        # Add the README and .gitignore files to the staging area
        subprocess.run(["git", "add", "README.md", ".gitignore"], cwd=os.path.join(repo_location, repo_name))
        
        # Commit the changes
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=os.path.join(repo_location, repo_name))
        
        # Add a remote named origin with the URL of the created repository using HTTPS
        subprocess.run(["git", "remote", "add", "origin", f"https://github.com/Betawarrior12/{repo_name}.git"], cwd=os.path.join(repo_location, repo_name))
        # Push to the main branch
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=os.path.join(repo_location, repo_name))
        
        print("Done")

    elif repo_create == "N":
        subprocess.run(["git", "init"], cwd=os.path.join(repo_location, repo_name))
        
        # Create a README file
        with open(os.path.join(repo_location, repo_name, "README.md"), "w") as f:
            f.write("# " + repo_name)
        
        # Create a .gitignore file
        with open(os.path.join(repo_location, repo_name, ".gitignore"), "w") as f:
            f.write("*.pyc\n__pycache__/\n")
        
        # Add the README and .gitignore files to the staging area
        subprocess.run(["git", "add", "README.md", ".gitignore"], cwd=os.path.join(repo_location, repo_name))
        
        # Commit the changes
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=os.path.join(repo_location, repo_name))
        
        # Add a remote named origin with the URL of the created repository using HTTPS
        subprocess.run(["git", "remote", "add", "origin", f"https://github.com/Betawarrior12/{repo_name}.git"], cwd=os.path.join(repo_location, repo_name))
        # Push to the main branch
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=os.path.join(repo_location, repo_name))

        print("Done")        

if __name__ == "__main__":
    main()
