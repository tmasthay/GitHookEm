import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from git_validator import GitValidator, sco, cprint


# Subclass
class PreCommitValidator(GitValidator):
    def base(self):
        current_branch = sco("git rev-parse --abbrev-ref HEAD")
        name_rev = sco("git name-rev --name-only HEAD")

        if current_branch == "main":
            if name_rev != "main" and 'main_allow' not in name_rev:
                cprint(
                    f"Error: Branch {name_rev} is not allowed to merge into"
                    " main."
                )
                sys.exit(1)


if __name__ == "__main__":
    PreCommitValidator(0).validate()
