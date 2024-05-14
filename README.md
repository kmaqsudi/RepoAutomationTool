
<p align="center">
  <img src="repoautomation-logo.jpeg" width="100" />
</p>
<p align="center">
    <h1 align="center">GitHub Repository Automation Setup</h1>
</p>
<p align="center">
    <em>Automate repo setup and push with ease!</em>
</p>
<p align="center">
    <img src="https://img.shields.io/github/license/kmaqsudi/RepoAutomationTool?style=flat&color=0080ff" alt="license">
    <img src="https://img.shields.io/github/last-commit/kmaqsudi/RepoAutomationTool?style=flat&color=0080ff" alt="last-commit">
    <img src="https://img.shields.io/github/languages/top/kmaqsudi/RepoAutomationTool?style=flat&color=0080ff" alt="repo-top-language">
    <img src="https://img.shields.io/github/languages/count/kmaqsudi/RepoAutomationTool?style=flat&color=0080ff" alt="repo-language-count">
</p>
<p align="center">
        <em>Developed with the software and tools below.</em>
</p>
<p align="center">
    <img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
    <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>
<hr>

## Introduction

This script automates the process of initializing a local project directory as a Git repository, creating a corresponding repository on GitHub, and pushing the local repository to GitHub. It's designed to be platform-agnostic, running on macOS, Debian-based, and RedHat-based systems, and uses environment variables for GitHub authentication, making the setup process seamless and efficient.

## Features

- Initializes a local Git repository
- Creates a new repository on GitHub (public or private as per user choice)
- Pushes the local repository to the newly created GitHub repository
- Simple and interactive user prompts
- Error handling for common issues
- Checks and installs necessary dependencies programmatically

## Prerequisites

- Git installed on your system
- A Personal Access Token (PAT) from GitHub with the necessary scopes
- `GITHUB_TOKEN` and `GITHUB_USERNAME` set as environment variables (or entered during script execution)

## Installation

### Bash Version

1. Download the script to your project directory.
2. Make the script executable:
   ```bash
   chmod +x create-github-repo-from-local-dir.sh
   ```
3. Ensure you have the necessary dependencies installed:
   - The script will check for `curl` and `jq` and prompt you to install them if they are missing.

### Python Version

1. Ensure you have Python installed on your system.
2. Install the required module:
   ```bash
   pip install requests
   ```
3. Download the script to your project directory.

## Usage

### Bash Version

1. Navigate to your project directory in the terminal.
2. Run the script:
   ```bash
   ./create-github-repo-from-local-dir.sh
   ```
3. Follow the interactive prompts to:
   - Set your GitHub Personal Access Token and Username if they are not already set as environment variables.
   - Specify whether the GitHub repository should be public or private.

### Python Version

1. Navigate to your project directory in the terminal.
2. Run the script:
   ```bash
   python create-github-repo-from-local-dir.py
   ```
3. Follow the interactive prompts to:
   - Enter your GitHub Personal Access Token and Username if they are not already set as environment variables.
   - Specify whether the GitHub repository should be public or private.

## Contributing

Contributions to improve this script are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

## License

This script is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Enjoy using the script! For any issues or suggestions, please open an issue in this repository.
