# GitHookEm
GitHookEm is a Python-based tool designed to be a starter kit for making your own custom hooks. 

![Git Hook Em Banner](hook_em.jpg)

## Making Custom Hooks with GitHookEm
`GitHookEm` provides a `GitValidator` ([example usage here](https://github.com/tmasthay/GitHookEm/blob/main/git_hook_em/pre_commit/ban_souper_secret.py)) class that allows for easy extension of custom hooks. 

Its interface just needs the `base` method for the core logic of how to validate.
To make it more extensible with subclasses, I also have empty implementations of a `pre` and `post` method and a `protocol` function to turn which of the three validation steps you wish to incorporate into the class. 
Nothing else is needed from you; all the interfacing with git to get things working is done through the base class.
See the [`gitvalidator.py`](https://github.com/tmasthay/GitHookEm/blob/main/git_hook_em/git_validator.py) file to see how everything works. 

## GitHookEm is a linear combination of `pre-commit` and `gitlint`
I use [`pre-commit`](https://pre-commit.com/) and [`gitlint`](https://jorisroovers.com/gitlint/latest/) as central dependencies. 
`gitlint` provides a class `CommitRule` ([example usage here](https://github.com/jorisroovers/gitlint/blob/main/examples/my_commit_rules.py)) similar to `GitValidator`, but it seems to only work on the `commit-msg` level.
`pre-commit` works on any commit stage, but does not provide a class similar to `GitValidator` or `CommitRule`.

The two points above are my motivation for this repo.

If I am mistaken about this or if there is yet another repo out there that provides a base class that works on all stages like `GitValidator`, then please let me know! 
Using that as a dependency would be a better design decision, given the relative minimalism and immaturity of `GitValidator`.

## Setup YAML files
To use my hooks, just add the following to your .pre-commit-config.yaml file at `REPO_PATH`
```bash
repos:
    - repo: https://github.com/tmasthay/GitHookEm
      rev: main  # The tag/commit to clone from
      hooks:
        - id: ban-super-secret
        - id: HOOK_ID_2
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

