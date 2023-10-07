import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from git_validator import GitValidator


class PreCommitValidator(GitValidator):
    def base(self):
        black_cmd = f"black -l 80 {self.root}"

        print(black_cmd)
        # 1. Run black to reformat code
        os.system(black_cmd)
        print("end black_cmd")

        # 2. Identify all files that were changed by black
        changed_files_output = os.popen("git diff --name-only").read().strip()
        changed_files = (
            changed_files_output.splitlines() if changed_files_output else []
        )

        # 3. Among the changed files, filter out only those which are currently being tracked by the repo
        tracked_files_output = os.popen("git ls-files").read().strip()
        tracked_files = (
            set(tracked_files_output.splitlines())
            if tracked_files_output
            else set()
        )

        for file in changed_files:
            if file in tracked_files:
                os.system(f"git add {file}")


if __name__ == "__main__":
    PreCommitValidator(0).validate()
