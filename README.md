# GitHookEm

GitHookEm is a Python-based tool designed to enforce and streamline git practices for code repositories. By setting up this tool in your git project, you can ensure consistent commit message conventions and code quality checks before pushes.

## Setup
To get setup
```bash
git clone https://github.com/tmasthay/GitHookEm.git
cd GitHookEm
pip install requirements.txt
(cd ..; pip install .)
```
The parentheses are currently **necessary**, but it's a hack I currently have due to a relative import issue that I am currently having. 
In theory, a slight modification from "python X.py" -> "python -m Y X.py" should do the trick, but I haven't fixed it yet. 
To setup the hooks of your cloned repo in respositories `foo` and `bar` with absolute paths `foo_path` and `bar_path`, run
```bash
cd /path/to/clone/of/GitHookEm
python git_validator.py foo_path
python git_validator.py bar_path
```
What this will do is setup **symbolic links to the cloned repo** in the appropriate path that git is expecting to look for hooks. 

The beauty of this is that now you can extend my repo to customize your own hooks within `/path/to/clone/of/GitHookEm` and you now have automatically synced all your repos
to your hook repos. 

I have implemented a few hooks for commit message validation and for pre-push validation as examples.

They are designed to be extensible, as they are both concretization of the abstract class `GitValidator`. 

**NOTE: PATH NAMES ARE IMPORTANT!**
For hook x-y, its implementation must be stored in x_y_validator! If you really hate this convention enough, modify the static method `make_symbolic_links` within the `GitValidator` class.

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
- Ensures that functions and classes have docstrings in committed Python files (currently has bugs).
