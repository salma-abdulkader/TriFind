import os

# --- Configuration ---
INDEX_FILE = "data/image_search.index"
METADATA_FILE = "data/image_search_metadata.json"
IMAGE_DIR = "data/data_images"  # Directory where images were indexed from
MODEL_ID = "openai/clip-vit-base-patch32"
HF_API_TOKEN = "YOUR_API_KEY"  # Define the HF API token
headers = {"Authorization": f"Bearer {HF_API_TOKEN}", "Content-Type": "audio/wav"}  # Define headers for HF API

if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)
    print(f"Created directory: {IMAGE_DIR}")


print(f"\n--- Upload Images for Indexing (to '{IMAGE_DIR}') ---")
