import torch
import numpy as np
from transformers import CLIPProcessor, CLIPModel, CLIPTokenizerFast
from PIL import Image

# Load CLIP model and tokenizer
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
clip_tokenizer = CLIPTokenizerFast.from_pretrained("openai/clip-vit-base-patch32")

# Generate embeddings for text
def get_text_embedding(text):
    inputs = clip_processor(text=[text], return_tensors="pt", padding=True)
    with torch.no_grad():
        embedding = clip_model.get_text_features(**inputs)
    return embedding.cpu().numpy()

# Generate embeddings for images
def get_image_embedding(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = clip_processor(images=image, return_tensors="pt")
    with torch.no_grad():
        embedding = clip_model.get_image_features(**inputs)
    return embedding.cpu().numpy()
