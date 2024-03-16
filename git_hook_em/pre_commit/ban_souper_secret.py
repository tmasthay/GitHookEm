import os

# import sys

# sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from git_hook_em.git_validator import GitValidator, cprint


class BanSuperSecret(GitValidator):
    def base(self):
        tracked_files = os.popen("git ls-files").read().strip()
        ban = "super_secret"
        for file in tracked_files:
            file = file.lower()
            ban2 = ban.replace("_", "")
            if ban in file or ban2 in file:
                cprint(
                    f'Now tracking "{file}" which has "{ban}" or "{ban2}" as a'
                    ' substring! Commit FAILED!'
                )
                exit(-1)


def main():
    BanSuperSecret(0).validate()


if __name__ == "__main__":
    main()
