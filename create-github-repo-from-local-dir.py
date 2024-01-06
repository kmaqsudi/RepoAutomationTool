#!/usr/bin/env python3

import os
import subprocess
import requests

# Check if necessary environment variables are set
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')

if not GITHUB_TOKEN:
    raise ValueError("GitHub Personal Access Token not set. Please set the GITHUB_TOKEN environment variable.")
if not GITHUB_USERNAME:
    raise ValueError("GitHub Username not set. Please set the GITHUB_USERNAME environment variable.")

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
def create_github_repo(repo_name, is_private):
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    data = {"name": repo_name, "private": is_private}
    
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    repo_url = response_json.get('clone_url')

    if not repo_url:
        print("Error creating GitHub repository. Response from GitHub API:")
        print(response_json)
        exit(1)

    print(f"Repository created: {repo_url}")
    return repo_url

# Function to initialize Git, commit all files, and link to GitHub
def initialize_and_push(repo_url):
    subprocess.run(['git', 'init'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Initial commit'])
    subprocess.run(['git', 'remote', 'add', 'origin', repo_url])
    result = subprocess.run(['git', 'push', '-u', 'origin', 'master'])

    if result.returncode != 0:
        print("Error pushing files to GitHub. Check your Git configuration and network connection.")
        exit(1)

# Main script execution starts here
repo_name = os.path.basename(os.getcwd())
is_private = get_repo_visibility()
repo_url = create_github_repo(repo_name, is_private)
initialize_and_push(repo_url)

print("Repository linked and files pushed to GitHub.")

