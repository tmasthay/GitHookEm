from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

# Read the requirements.txt file
with open("requirements.txt", "r") as fh:
    requirements = [
        line.strip() for line in fh if line.strip() and not line.startswith("#")
    ]

setup(
    name="GitHookEm",
    version="0.1.0",
    author="Tyler",
    author_email="tyler@example.com",
    description="A package for git hooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tmasthay/GitHookEm",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    scripts=["update_imports.py"],
    entry_points={
        'console_scripts': [
            (
                'commit-msg-directives='
                'git_hook_em.commit_msg_validator.commit_msg_validator:main'
            ),
            'ban-super-secret=git_hook_em.pre_commit_validator:main',
        ]
    },
)
