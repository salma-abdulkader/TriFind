import os
import json
import faiss
import numpy as np
from .clip_model import get_image_embedding

# Create FAISS index from dataset
def create_faiss_index(image_folder, index_file, metadata_file):
    embeddings = []
    metadata = []

    for image_name in os.listdir(image_folder):
        image_path = os.path.join(image_folder, image_name)
        embedding = get_image_embedding(image_path)
        embeddings.append(embedding)
        metadata.append(image_name)

    embeddings = np.vstack(embeddings).astype("float32")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, index_file)
    with open(metadata_file, "w") as f:
        json.dump(metadata, f)
    print(f"✅ FAISS index created: {index_file}")

# Load FAISS index
def load_faiss_index(index_file, metadata_file):
    index = faiss.read_index(index_file)
    with open(metadata_file, "r") as f:
        metadata = json.load(f)
    return index, metadata

# Search in FAISS index
def search_faiss(query_embedding, index, metadata, top_k=5):
    D, I = index.search(query_embedding.astype("float32"), top_k)
    results = [(metadata[i], float(D[0][idx])) for idx, i in enumerate(I[0])]
    return results
