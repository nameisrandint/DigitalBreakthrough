import os

__file_path = os.path.realpath(__file__)  # abs path to this script
__file_parent_dir = os.path.dirname(__file_path)
BOTS_CACHE_DIRNAME = '.bots_cache'
BOTS_CACHE_DIR = os.path.join(__file_parent_dir, BOTS_CACHE_DIRNAME)
assert os.path.exists(BOTS_CACHE_DIR), \
    f'Not exists: "{BOTS_CACHE_DIR}". Create {BOTS_CACHE_DIRNAME}/ directory by the path'
