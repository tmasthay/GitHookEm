# hello.py
import sys

def main(commit_msg_file_path):
    with open(commit_msg_file_path, 'r') as f:
        commit_msg = f.read().strip()
    print(f"Hello World - Commit message is: {commit_msg}", flush=True)

if __name__ == "__main__":
    main(sys.argv[1])

