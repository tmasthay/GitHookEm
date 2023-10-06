from setuptools import setup, find_packages

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
    author_email="tyler@example.com",  # replace with your email
    description="A package for git hooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tmasthay/GitHookEm",  # replace with your repo URL
    packages=find_packages(),  # This will find packages automatically
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # or any other license you're using
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # or the minimum version you support
    install_requires=requirements,
    scripts=['update_imports.py'],
)
