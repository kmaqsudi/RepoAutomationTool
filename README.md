
# GitHub Repository Setup Script

## Introduction

This script automates the process of initializing a local project directory as a Git repository, creating a corresponding repository on GitHub, and pushing the local repository to GitHub. It's designed for macOS users and uses environment variables for GitHub authentication, making the setup process seamless and efficient.

## Features

- Initializes a local Git repository.
- Creates a new repository on GitHub (public or private as per user choice).
- Pushes the local repository to the newly created GitHub repository.
- Simple and interactive user prompts.
- Error handling for common issues.

## Prerequisites

- Git installed on your macOS.
- A Personal Access Token (PAT) from GitHub with the necessary scopes.
- `GITHUB_TOKEN` and `GITHUB_USERNAME` set as environment variables.
```bash
   # add the following lines to your .bash_profile or .zprofile
   export GITHUB_USERNAME="user@gmail.com"
   export GITHUB_TOKEN="github-token-generated-with-correct-scopes"
   ```

## Installation

1. Download the script to your project directory.
2. Make the script executable:
   ```bash
   chmod +x setup_git_repo.sh
   ```
3. Ensure that your GitHub username and personal access token are set as environment variables:
   ```bash
   export GITHUB_TOKEN=your_token_here
   export GITHUB_USERNAME=your_github_username
   ```

## Usage

1. Navigate to your project directory in the terminal.
2. Run the script:
   ```bash
   ./setup_git_repo.sh
   ```
3. Follow the interactive prompts to specify whether the GitHub repository should be public or private.

## Contributing

Contributions to improve this script are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

## License

This script is released under the MIT License. See the [LICENSE](LICENSE) file for more details.


---

Enjoy using the script! For any issues or suggestions, please open an issue in this repository.
