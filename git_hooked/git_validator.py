from subprocess import check_output as co
from abc import ABC, abstractmethod
import os
import sys
from termcolor import colored


# Helper function for parsing cli
# This comment should not appear in main branch
def sco(s):
    try:
        return co(s, shell=True).decode("utf-8").strip()
    except:
        raise


def cprint(s, color="red", **kw):
    print(colored(s, color), **kw)


# ignore
class GitValidator(ABC):
    def __init__(self, nargs=1):
        self.nargs = nargs

    @abstractmethod
    def base(self, *args, **kw):
        raise NotImplementedError(
            "base is not implemented. "
            "This message should never be seen since base is abstract."
        )

    def pre(self, *args, **kw):
        raise NotImplementedError(
            "pre is not implemented. If you do intend to use it, ensure that"
            " protocol() reflects this. Else, implement custom_pre in the child"
            " class."
        )

    def post(self, *args, **kw):
        raise NotImplementedError(
            "post is not implemented. If you do intend to use it, ensure that"
            " protocol() reflects this. Else, implement custom_post in the"
            " child class."
        )

    def protocol(self, *args, **kw):
        return dict(pre=False, base=True, post=False)

    def _validate(self, *args, **kw):
        protocol = self.protocol(*args, **kw)
        if protocol["pre"]:
            self.pre(*args, **kw)
        if protocol["base"]:
            self.base(*args, **kw)
        if protocol["post"]:
            self.post(*args, **kw)

    def validate(self):
        args, kw = self.parse_sys_argv(sys.argv)
        self._validate(*args, **kw)

    def _parse_sys_argv(self, argv):
        return argv[1 : (1 + self.nargs)], dict()

    def parse_sys_argv(self, argv):
        if len(argv) <= self.nargs:
            print(f"Expected at least {self.nargs} arguments, got {len(argv)}")
            sys.exit(1)
        args, kw = self._parse_sys_argv(argv)
        return args, kw

    @staticmethod
    def make_symbolic_links(repo_root, exclude_dirs=None):
        if exclude_dirs is None:
            exclude_dirs = ["__pycache__"]
        hooks_root = os.path.dirname(os.path.abspath(__file__))
        _, subdir, _ = next(os.walk(hooks_root))
        subdir = [e for e in subdir if e not in exclude_dirs]
        for d in subdir:
            d_abs = os.path.join(hooks_root, d)
            repo_hook_name = d.replace("_validator", "").replace("_", "-")
            repo_hook_path = os.path.join(repo_root, ".git", "hooks")
            if not os.path.exists(repo_hook_path):
                raise FileNotFoundError(
                    f"{repo_hook_path} does not exist.\n"
                    f"Please ensure that {repo_root} is a git repository."
                )
            repo_hook_path = os.path.join(repo_hook_path, repo_hook_name)
            hooks_dummy_path = os.path.join(d_abs, f"{d}_dummy.sh")
            py_path = os.path.join(d_abs, f"{d}.py")
            if os.path.exists(repo_hook_path) and not os.path.islink(repo_hook_path):
                raise FileExistsError(
                    f"{repo_hook_path} exists and is not a symbolic link."
                    " Exiting since proceeding is potentially dangerous. If"
                    f" you wish to overwrite {repo_hook_path}, manually delete"
                    " it from your repo and re-run this script."
                )
            elif os.path.exists(repo_hook_path) and os.path.islink(repo_hook_path):
                if os.path.realpath(repo_hook_path) != hooks_dummy_path:
                    raise FileExistsError(
                        f"{repo_hook_path} exists and is incorrectly linked to"
                        f" {os.path.realpath(repo_hook_path)} instead of"
                        f" {hooks_dummy_path}. Exiting since proceeding is"
                        " potentially dangerous. If you wish to overwrite"
                        " {repo_hook_path}, manually delete it from your"
                        " repo and re-run this script."
                    )
                else:
                    print(
                        f"{repo_hook_path} already exists and is correctly"
                        f" symbolically linked to {d_abs}...skipping."
                    )
            else:
                if not os.path.exists(hooks_dummy_path):
                    file_contents = f"#!/usr/bin/bash\npython {py_path} $@"
                    print(
                        f"{hooks_dummy_path} does not exist...creating dummy"
                        f" file with contents given below\n{file_contents}"
                    )
                    with open(hooks_dummy_path, "w") as f:
                        f.write(file_contents)
                    os.system(f"chmod +x {hooks_dummy_path}")
                print(
                    f"{repo_hook_path} does not exist...creating symbolic link"
                    f" to {d_abs}."
                )
                os.symlink(hooks_dummy_path, repo_hook_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python git_validator.py <repo_root>")
        sys.exit(1)
    repo_root = sys.argv[1]
    GitValidator.make_symbolic_links(repo_root)
