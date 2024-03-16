import os
import sys
from abc import ABC, abstractmethod
from subprocess import check_output as co

from termcolor import colored


# Helper function for parsing cli
# This comment should not appear in main branch
def sco(s):
    try:
        return co(s, shell=True).decode("utf-8").strip()
    except Exception as e:
        raise e


def cprint(s, color="red", **kw):
    print(colored(s, color), **kw)


# ignore
class GitValidator(ABC):
    def __init__(self, nargs=1):
        self.nargs = nargs
        self.root = GitValidator.get_root()

    @staticmethod
    def get_root():
        return sco("git rev-parse --show-toplevel")

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
