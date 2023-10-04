import os
import sys
from masthay_helpers.import_env import *

include_paths = ['git_hooks']

# run_make_files(omissions)

init_modules(os.getcwd(), root=True, inclusions=include_paths, unload=True)
