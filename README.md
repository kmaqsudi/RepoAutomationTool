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
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>
<hr>

## Introduction

This Python script automates the process of initializing a local project directory as a Git repository, creating a corresponding repository on GitHub, and pushing the local repository to GitHub. It is designed to be user-friendly and efficient, with interactive prompts and automatic dependency handling.

## Features

- **Interactive Setup**: Prompts for GitHub credentials if not set as environment variables.
- **Automatic Dependency Installation**: Checks for and installs required Python libraries.
- **Initializes a local Git repository**: Uses `main` as the default branch.
- **Creates a new repository on GitHub**: Supports public or private repositories.
- **Pushes the local repository**: Links and pushes your code to the newly created GitHub repository.
- **User-Friendly**: Simple and clear interactive prompts.
- **Error Handling**: Provides informative error messages for common issues.

## Prerequisites

- **Python 3**: The script is written in Python 3.
- **Git**: Git must be installed on your system.
- **GitHub Account**: A GitHub account is required to create repositories.

## Installation

1.  Download the `create-github-repo-from-local-dir.py` script to your project directory.
2.  Make the script executable (optional, but recommended):
    ```bash
    chmod +x create-github-repo-from-local-dir.py
    ```

## Usage

1.  Navigate to your project directory in the terminal.
2.  Run the script:
    ```bash
    python3 create-github-repo-from-local-dir.py
    ```
    or if you made it executable:
    ```bash
    ./create-github-repo-from-local-dir.py
    ```
3.  Follow the interactive prompts:
    - If the `requests` library is not installed, the script will ask for your permission to install it.
    - If your `GITHUB_TOKEN` and `GITHUB_USERNAME` are not set as environment variables, the script will prompt you to enter them.
    - You will be asked if you want your new repository to be public or private.

---

### A Note on the Shell Script

The `create-github-repo-from-local-dir.sh` script is now deprecated. The Python script (`create-github-repo-from-local-dir.py`) is the recommended tool as it is more robust, feature-rich, and user-friendly.

---

## Contributing

Contributions to improve this script are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

## License

This script is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Enjoy using the script! For any issues or suggestions, please open an issue in this repository.
