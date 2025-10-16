import os
import shutil

def ensure_dir_exists(directory):
    """Create a directory if it doesn't exist."""
    os.makedirs(directory, exist_ok=True)

def copy_if_missing(src, dst):
    """Copy a file only if it doesn't already exist at destination."""
    if not os.path.exists(dst) and os.path.exists(src):
        shutil.copy(src, dst)

def print_banner():
    """Optional banner to confirm app startup."""
    print("\n🚀 Multimodal Search System Initialized Successfully!\n")