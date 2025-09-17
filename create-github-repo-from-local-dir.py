#!/usr/bin/env python3

import os
import subprocess
import sys

# Function to check and install dependencies
def check_and_install_dependencies():
    try:
        import requests
    except ImportError:
        print("The 'requests' library is not installed.")
        response = input("Would you like to install it now? (y/n): ").lower()
        if response in ['y', 'yes']:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
                print("'requests' library installed successfully.")
            except subprocess.CalledProcessError:
                print("Error: Could not install 'requests'. Please install it manually and run the script again.")
                exit(1)
        else:
            print("The 'requests' library is required to run this script.")
            exit(1)

# Main script execution starts here
check_and_install_dependencies()

import requests

# Function to get GitHub credentials
def get_github_credentials():
    token = os.getenv('GITHUB_TOKEN')
    username = os.getenv('GITHUB_USERNAME')

    if not token:
        token = input("Please enter your GitHub Personal Access Token: ")
    if not username:
        username = input("Please enter your GitHub Username: ")

    return token, username

# Prompt user for public or private repository choice
def get_repo_visibility():
    while True:
        response = input("Do you want your GitHub repository to be public? (y/n): ").lower()
        if response in ['y', 'yes']:
            return False
        elif response in ['n', 'no']:
            return True
        else:
            print("Please answer yes (y) or no (n).")

# Function to create a GitHub repository using the GitHub API
def create_github_repo(repo_name, is_private, token):
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {token}"}
    data = {"name": repo_name, "private": is_private}
    
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    if response.status_code == 201:
        repo_url = response_json.get('clone_url')
        print(f"Repository created: {repo_url}")
        return repo_url
    else:
        print("Error creating GitHub repository. Response from GitHub API:")
        print(response_json.get("message", "No message provided"))
        for error in response_json.get("errors", []):
            print(f"- {error.get('message')}")
        exit(1)

# Function to initialize Git, commit all files, and link to GitHub
def initialize_and_push(repo_url):
    # Check if git is initialized
    if not os.path.exists(".git"):
        subprocess.run(['git', 'init', '-b', 'main'])
        print("Initialized a new git repository with 'main' branch.")
    else:
        print("Git repository already exists.")

    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Initial commit'])

    # Check if remote 'origin' already exists
    remotes = subprocess.check_output(['git', 'remote']).decode().strip().split('\n')
    if 'origin' not in remotes:
        subprocess.run(['git', 'remote', 'add', 'origin', repo_url])

    result = subprocess.run(['git', 'push', '-u', 'origin', 'main'])

    if result.returncode != 0:
        print("Error pushing files to GitHub. Check your Git configuration and network connection.")
        exit(1)

# Main function
def main():
    repo_name = os.path.basename(os.getcwd())
    token, username = get_github_credentials()
    is_private = get_repo_visibility()
    repo_url = create_github_repo(repo_name, is_private, token)
    initialize_and_push(repo_url)
    print("Repository linked and files pushed to GitHub successfully.")

if __name__ == "__main__":
    main()
