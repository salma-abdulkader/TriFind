# 🔍 Multimodal Search System (Text + Image + Voice)

A multimodal AI system that allows **text**, **image**, and **voice** search — powered by CLIP, FAISS, Whisper, and SpeechT5.  
Developed in Python using Hugging Face Transformers and Gradio for the interface.

---

## 🚀 Features

- 🧠 **Text & Image Embeddings** using OpenAI’s CLIP model  
- 🎤 **Speech-to-Text** with Whisper (via Hugging Face API)  
- 🗣️ **Text-to-Speech** with Microsoft SpeechT5  
- 🔎 **Vector Search** powered by FAISS  
- 💬 **Sentiment Feedback System** to collect and analyze user impressions  with DistilBERT
- 🖼️ **Interactive Gradio Interface** for seamless multimodal queries  

---

## 🧩 Folder Structure

```
TriFind/
│
├── app/
│ ├── main.py
│ ├── config.py
│ └── setup.py
│
├── models/
│ ├── clip_model.py
│ ├── faiss_index.py
│ ├── whisper_api.py
│ ├── sentiment_feedback.py
│ └── tts_model.py
│
├── utils/
│ └── helpers.py
│
├── data/
│ ├── data_images/
│ ├── image_search.index
│ ├── image_search_metadata.json
│ └── user_feedback.txt
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```
# Clone the repository
git clone https://github.com/yourusername/multimodal-search.git
cd multimodal-search


# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

python app/main.py

export HF_API_TOKEN="your_token_here"

setx HF_API_TOKEN "your_token_here"
```

🗂️ Data Folder
  data/data_images/ → Place your reference images here.
  data/image_search.index → Created automatically when the index is built.
  data/image_search_metadata.json → Stores filenames for search results.
  data/user_feedback.txt → Stores user feedback and sentiment scores.


📜 License
This project is open-source under the MIT License.
