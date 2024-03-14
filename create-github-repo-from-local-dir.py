import os
import subprocess
import requests

def check_shell_and_profile():
    """Determines the user's shell and corresponding profile file."""
    shell = os.environ.get('SHELL')
    if 'bash' in shell:
        return '.bash_profile'
    elif 'zsh' in shell:
        return '.zprofile'
    else:
        print("Unsupported shell.")
        exit(1)

def check_variable_in_profile(profile, variable):
    """Checks if an environment variable exists in the profile file."""
    try:
        with open(os.path.expanduser(f'~/{profile}'), 'r') as file:
            if any(line.strip().startswith(f'export {variable}=') for line in file):
                return True
    except FileNotFoundError:
        pass
    return False

def add_variable_to_profile(profile, variable, value):
    """Adds an environment variable to the profile file and current session."""
    with open(os.path.expanduser(f'~/{profile}'), 'a') as file:
        file.write(f'\nexport {variable}="{value}"\n')
    os.environ[variable] = value  # Add the variable to the current environment


profile = check_shell_and_profile()

# Request GitHub token if not set or found in the profile
if not check_variable_in_profile(profile, 'GITHUB_TOKEN') or not os.getenv('GITHUB_TOKEN'):
    github_token = input("Enter your GitHub token: ")
    add_to_profile = input("Would you like to add it to your shell profile? (yes/no): ").lower()
    if add_to_profile == 'yes':
        add_variable_to_profile(profile, 'GITHUB_TOKEN', github_token)
    os.environ['GITHUB_TOKEN'] = github_token  # Set for current process

# Request GitHub username if not set or found in the profile
if not check_variable_in_profile(profile, 'GITHUB_USERNAME') or not os.getenv('GITHUB_USERNAME'):
    github_username = input("Enter your GitHub username: ")
    add_to_profile = input("Would you like to add it to your shell profile? (yes/no): ").lower()
    if add_to_profile == 'yes':
        add_variable_to_profile(profile, 'GITHUB_USERNAME', github_username)
    os.environ['GITHUB_USERNAME'] = github_username  # Set for current process

# Now, we're sure that github_token and github_username are available for the script's process
github_token = os.getenv('GITHUB_TOKEN')
github_username = os.getenv('GITHUB_USERNAME')

# Only prompt for the GitHub token and username if they are not already set.
if not github_token:
    if check_variable_in_profile(profile, 'GITHUB_TOKEN'):
        print("Using GitHub credentials stored in your shell profile.")
    else:
        github_token = input("Enter your GitHub token: ")
        add_to_profile = input("Would you like to add it to your shell profile? (yes/no): ").lower()
        if add_to_profile == 'yes':
            add_variable_to_profile(profile, 'GITHUB_TOKEN', github_token)

if not github_username:
    if check_variable_in_profile(profile, 'GITHUB_USERNAME'):
        print("Using GitHub credentials stored in your shell profile.")
    else:
        github_username = input("Enter your GitHub username: ")
        add_to_profile = input("Would you like to add it to your shell profile? (yes/no): ").lower()
        if add_to_profile == 'yes':
            add_variable_to_profile(profile, 'GITHUB_USERNAME', github_username)

# Ensure the token and username are available for the GitHub API interaction.
if not github_token or not github_username:
    raise ValueError("GitHub credentials not set. Please set the GITHUB_TOKEN and GITHUB_USERNAME environment variables.")

def get_repo_visibility():
    """Prompts user for repository visibility choice."""
    while True:
        response = input("Do you want your GitHub repository to be public? (y/n): ").lower()
        if response in ['y', 'yes']:
            return False
        elif response in ['n', 'no']:
            return True
        else:
            print("Please answer yes (y) or no (n).")

def create_github_repo(repo_name, is_private):
    """Creates a GitHub repository using the GitHub API."""
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {github_token}"}
    data = {"name": repo_name, "private": is_private}
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 201:  # 201 Created
        print("Error creating GitHub repository. Response from GitHub API:")
        print(response.json())
        exit(1)

    repo_url = response.json().get('clone_url')
    print(f"Repository created: {repo_url}")
    return repo_url

def initialize_and_push(repo_url):
    """Initializes git, commits all files, and pushes to the created GitHub repository."""
    subprocess.run(['git', 'init'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Initial commit'])
    subprocess.run(['git', 'branch', '-M', 'main'])  # Ensure default branch is 'main'
    subprocess.run(['git', 'remote', 'add', 'origin', repo_url])
    subprocess.run(['git', 'push', '-u', 'origin', 'main'])

# Main script execution starts here.
repo_name = input("Enter the name of your repository: ")
is_private = get_repo_visibility()
repo_url = create_github_repo(repo_name, is_private)
initialize_and_push(repo_url)

print("Repository linked and files pushed to GitHub.")

