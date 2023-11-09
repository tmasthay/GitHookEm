# GitHookEm

GitHookEm is a Python-based tool designed to be a starter kit for making your own custom hooks. 

## Setup YAML files
To use my hooks, just add the following to your .pre-commit-config.yaml file at `REPO_PATH`
```bash
repos:
    - repo: https://github.com/tmasthay/GitHookEm
      rev: main  # The tag/commit to clone from
      hooks:
        - id: commit-msg-directives
        - id: HOOK_EM_ID_2
      .
      .
      .
      REST OF YAML FILE
```
Currently support `GitHookEm` ids are below.
| id | Description          | See for reference |
|----|----------------------| -------------- | 
| commit-msg-directives | Force ALL_CAPS directives at beginning of commit messages, similar to `commitizen`.  | `git_hook_em.commit_msg.directives.main()`
| ban-super-secret | Check for file with `super_secret` as a substring, in case `.gitignore` error occurred. | `git_hook_em.pre_commit.ban_souper_secret.main()`

## Setup pre-commit
GitHookEm uses `pre-commit`, which is straightforward to setup. Directions are below.

```bash
pip install pre-commit
cd path_to_your_repo
pre-commit install
```
Now try `git commit --allow-empty` and see how it works! Email me at tyler@oden.utexas.edu if you need help setting up!

## Other suggested hooks
There are a lot of hooks on GitHub already out there that are easy to plugin once you are setup.

Try to avoid making custom hooks unless you absolutely **need** to; it just saves time and headaches.

See my [.pre-commit-config.yaml file](https://github.com/tmasthay/GitHookEm/blob/main/.pre-commit-config.yaml) for a starter kit. 

Below is a table briefly describing the hooks external to this repo.  

| Name | Description | Github page |
| ------- | ------------------------ | ------------------------- |
| black | Opinionated Python style formatter | [black GitHub](https://github.com/psf/black) |
| pre-commit | Framework for managing git hooks | [pre-commit GitHub](https://github.com/pre-commit/pre-commit) and [pre-commit hooks](https://github.com/pre-commit/pre-commit-hooks) |
| isort | Sorts Python imports alphabetically | [isort GitHub](https://github.com/pycqa/isort) |
| flake8 | Python linter and style guide | [flake8 GitHub](https://github.com/pycqa/flake8) |
| yamllint | YAML linter | [yamllint GitHub](https://github.com/adrienverge/yamllint.git) |


