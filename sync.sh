#!/bin/bash

gsrt(){
    local super=$(git rev-parse --show-superproject-working-tree)
    if [ -z $super ]; then
        echo "$(git rev-parse --show-toplevel)"
    else
        echo "$super"
    fi
}

prev=$(pwd)
cd $(gsrt) || {
    echo "Error: Unable to find the top-level directory of a Git repository."
    exit 1
}

last_part=$(pwd | awk -F'/' '{print $NF}')

if [ "$last_part" == "GitHookEm" ]; then
    echo "Error: This script should not be run from within the GitHookEm directory."
    exit 1
fi

git submodule update --recursive --remote

cd GitHookEm || {
    echo "Error: Unable to find the GitHookEm directory."
    exit 1
}

# Additional custom actions can be placed here
VALS_TO_COPY_UP=$(
    find . -name ".*" | \
    awk -F'/' {'print $2}' | \
    xargs -n1 | \
    grep -vE "^(.git|.gitignore|.pre-commit-hooks.yaml)$"
)

for VAL in $VALS_TO_COPY_UP; do
    echo "Copying $VAL"
    cp -r "$VAL" ..
done
cd ..
if [ ! -f .git/hooks/commit-msg-backup ]; then
    mv .git/hooks/commit-msg .git/hooks/commit-msg-backup
fi
gitlint install-hook

verbose=${1:-false}
if [ "$verbose" == "-v" ]; then
    pre-commit clean
    pre-commit install --verbose
else
    pre-commit clean 2> /dev/null 2>&1
    pre-commit install 2> /dev/null 2>&1
fi

cd $prev
