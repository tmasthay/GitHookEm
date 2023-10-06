# GitHooked

GitHooked is a Python-based tool designed to enforce and streamline git practices for code repositories. By setting up this tool in your git project, you can ensure consistent commit message conventions and code quality checks before pushes.

## Components

### Git Validator (`git_validator.py`):

- Provides a base class `GitValidator` for creating custom git hook validators.
- Contains helper functions for parsing command-line input and symbolic link creation for hooks.
- When run as a main script, it sets up symbolic links for all git hooks present in the repository.

### Commit Message Validator (`commit_msg_validator.py`):

- Ensures commit messages follow specific formats and conventions.
- Commit messages should start with predefined directives followed by a description. Some of the supported directives include `BUG`, `FEATURE`, `DEBUG`, and more.

### Pre-Push Validator (`pre_push_validator.py`):

- Validates code with `black` for Python formatting conventions.
- Ensures that functions and classes have docstrings in committed Python files.

## Usage

### Setting up Git Validator

1. Navigate to your repository root.
2. Run the `git_validator.py` script, providing your repository root as an argument.
   ```bash
   python git_validator.py <path_to_repo_root>
   ```

### Commit Message Validator

1. When you commit, the `commit_msg_validator.py` script will automatically validate your commit message against the defined conventions.

### Pre-Push Validator

1. Before pushing, the `pre_push_validator.py` script will validate your code using `black` and check for the presence of docstrings in your Python files.

## Notes

- Ensure you have the required packages installed, including `termcolor` and other dependencies mentioned in the scripts.
- This project uses abstract base classes; ensure you are familiar with them when extending or modifying the base validators.

## Contributing

Contributions are welcome! Please follow the conventions defined in the `commit_msg_validator` when making commit messages.
