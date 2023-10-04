import os
import sys
from git_validator import GitValidator


class PrePushValidator(GitValidator):
    def base(self):
        # 1. Check with black
        black_result = os.system("black --check .")
        if black_result != 0:
            print("Error: Code does not adhere to black's conventions!")
            exit(1)

        # 2. Check for docstrings in committed Python files
        changed_files = os.popen("git diff --name-only").read().splitlines()
        python_files = [f for f in changed_files if f.endswith(".py")]

        for py_file in python_files:
            with open(py_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if "def " in line or "class " in line:
                        next_line = lines[lines.index(line) + 1].strip()
                        if not next_line.startswith('"""'):
                            print(
                                f"Error: Missing docstring in {py_file} for"
                                f" definition: {line.strip()}"
                            )
                            exit(1)


if __name__ == "__main__":
    PrePushValidator().validate()
