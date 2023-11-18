# GitHookEm
![Git Hook Em Banner](hook_em.jpg)

GitHookEm is a Python-based tool designed to be a starter kit for making your own custom hooks. 

## Making Custom Hooks with GitHookEm
`GitHookEm` provides a `GitValidator` class that allows for easy extension of custom hooks. 
Its interface just needs the `validate` method to determine if the git stage should continue to execute or not. 
See the `gitvalidator.py` file to see how it works. 
I am considering refactoring this entirely into another framework like `gitlint`.
From what I understand, `gitlint` is meant for commit-msg parsing though rather than all stages, and I need to read more to verify.
I also need to check if `pre-commit` has classes similar to `gitlint` as well. 
If there were something that allows both `gitlint`'s easy extensibility and `pre-commit`'s great YAML management, then I will likely perform the refactor out my `GitValidator` class, and this repo will essentially transform into a tutorial on how to use that package.

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
| ban-super-secret | Check for file with `super_secret` as a substring, in case `.gitignore` error occurred. | [ban_souper_secret.py](https://github.com/tmasthay/GitHookEm/blob/main/git_hook_em/pre_commit/ban_souper_secret.py) |

## Setup pre-commit
GitHookEm uses `pre-commit`, which is straightforward to setup. Directions are below.

```bash
pip install pre-commit
cd repo_root
pre-commit install
```
Now try `git commit --allow-empty` and see how it works! Email me at tyler@oden.utexas.edu if you need help setting up!

## Setup gitlint
`GitHookEm` also supports a `gitlint` extension for commit message formating, similar to `commitizen`. To set this up, perform the following steps.
First, backup or remove your previous commit-msg executable.
```
cd repo_root
mv .git/hooks/commit-msg .git/hooks/commit-msg-backup
```
Then put the `gitlint` hidden files in the repository's root directory and then install the hook; this installation creates a file in `.git/hooks/commit-msg`.
```
cp git_hook_em_path/.gitlint .
cp -r git_hook_em_path/.gitlint_rules .
gitlint install-hook
```

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

