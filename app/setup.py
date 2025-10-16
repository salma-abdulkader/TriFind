import os, shutil

# 1. Source (Kaggle dataset path)
source_image_directory = '/kaggle/input/fashion-product-images-dataset/fashion-dataset/images/'
IMAGE_DIR = "data/data_images"

# --- Setup: Create Destination Directory ---
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)
    print(f"Created destination directory: {IMAGE_DIR}")

# --- Copy Images from Source to Destination ---
print(f"Starting to copy images from {source_image_directory} to {IMAGE_DIR}...")

copied_count = 0
total_files_in_source = 0

for dirname, _, filenames in os.walk(source_image_directory):
    total_files_in_source += len(filenames)
    for filename in filenames:
        src_path = os.path.join(dirname, filename)
        dst_path = os.path.join(IMAGE_DIR, filename)
        try:
            shutil.copy(src_path, dst_path)
            copied_count += 1
        except Exception as e:
            print(f"Warning: Could not copy file {filename}: {e}")

print(f"\nFinished copying. Total files found in source: {total_files_in_source}")
print(f"Successfully copied {copied_count} files to {IMAGE_DIR}.")
