#!/usr/bin/env bash

# This script automates the process of initializing a local project directory as a Git repository,
# creating a corresponding repository on GitHub, and pushing the local repository to GitHub.
# Author: Khalid Maqsudi
# Date: 12-11-2023
# v2 error handling added:  05-14-2024

# Function to check if a command exists and prompt for installation if missing
check_dependency() {
    local cmd=$1
    if ! command -v "$cmd" > /dev/null; then
        echo "Error: $cmd is not installed."
        while true; do
            read -p "Do you want to install $cmd? (y/n): " yn
            case $yn in
                [Yy]* )
                    if [ "$(uname)" == "Darwin" ]; then
                        # macOS
                        if ! command -v brew > /dev/null; then
                            echo "Homebrew is not installed. Installing Homebrew first..."
                            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
                        fi
                        brew install "$cmd"
                    elif [ -f /etc/debian_version ]; then
                        # Debian-based system
                        sudo apt-get update
                        sudo apt-get install -y "$cmd"
                    elif [ -f /etc/redhat-release ]; then
                        # RedHat-based system
                        sudo yum install -y "$cmd"
                    else
                        echo "Unsupported OS. Please install $cmd manually."
                        exit 1
                    fi
                    break;;
                [Nn]* ) echo "$cmd is required. Exiting."; exit 1;;
                * ) echo "Please answer yes (y) or no (n).";;
            esac
        done
    fi
}

# Function to check if necessary environment variables are set and prompt for input if missing
check_env_variables() {
    if [ -z "$GITHUB_TOKEN" ]; then
        read -p "GitHub Personal Access Token is not set. Please enter your GitHub Personal Access Token: " GITHUB_TOKEN
        if [ -z "$GITHUB_TOKEN" ]; then
            echo "GitHub Personal Access Token is required. Exiting."
            exit 1
        fi
        export GITHUB_TOKEN
    fi

    if [ -z "$GITHUB_USERNAME" ]; then
        read -p "GitHub Username is not set. Please enter your GitHub Username: " GITHUB_USERNAME
        if [ -z "$GITHUB_USERNAME" ]; then
            echo "GitHub Username is required. Exiting."
            exit 1
        fi
        export GITHUB_USERNAME
    fi
}

# Function to prompt user for public or private repository choice
get_repo_visibility() {
    while true; do
        read -p "Do you want your GitHub repository to be public? (y/n): " yn
        case $yn in
            [Yy]* ) is_private="false"; break;;
            [Nn]* ) is_private="true"; break;;
            * ) echo "Please answer yes (y) or no (n).";;
        esac
    done
}

# Function to create a GitHub repository using the GitHub API
create_github_repo() {
    local repo_name=$1
    local is_private=$2

    echo "Creating GitHub repository $repo_name..."
    create_repo_response=$(curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
        -d "{\"name\":\"$repo_name\", \"private\": $is_private}" \
        "https://api.github.com/user/repos")

    # Extract the URL of the created repository
    if command -v jq > /dev/null; then
        repo_url=$(echo "$create_repo_response" | jq -r '.clone_url')
    else
        repo_url=$(echo "$create_repo_response" | grep '"clone_url"' | cut -d '"' -f 4)
    fi

    if [ -z "$repo_url" ]; then
        echo "Error creating GitHub repository. Response from GitHub API:"
        echo "$create_repo_response"
        exit 1
    fi

    echo "Repository created: $repo_url"
}

# Function to initialize Git, commit all files, and link to GitHub
initialize_and_push() {
    local repo_url=$1

    echo "Initializing Git repository and committing files..."
    git init
    git add .
    git commit -m "Initial commit"

    echo "Linking to GitHub repository and pushing files..."
    git remote add origin "$repo_url"
    git push -u origin master

    if [ $? -ne 0 ]; then
        echo "Error pushing files to GitHub. Check your Git configuration and network connection."
        exit 1
    fi
}

# Main script execution starts here

# Check if necessary dependencies are installed
check_dependency "curl"
check_dependency "jq"

# Check if necessary environment variables are set
check_env_variables

# Get the current directory name to use as the repository name
repo_name=$(basename "$(pwd)")

# Prompt user for repository visibility (public/private)
get_repo_visibility

# Create a GitHub repository
create_github_repo "$repo_name" "$is_private"

# Initialize local repository, commit, and push to GitHub
initialize_and_push "$repo_url"

echo "Repository linked and files pushed to GitHub."

