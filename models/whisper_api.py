import requests
import io
import soundfile as sf
import os

# Whisper speech-to-text function
def transcribe_speech(audio):
    HF_API_TOKEN = os.getenv("HF_API_TOKEN", "")
    if not HF_API_TOKEN:
        raise ValueError("Missing HF_API_TOKEN in environment variables.")

    audio_bytes = io.BytesIO()
    sf.write(audio_bytes, audio[1], audio[0], format="WAV")
    audio_bytes.seek(0)

    response = requests.post(
        "https://api-inference.huggingface.co/models/openai/whisper-base",
        headers={"Authorization": f"Bearer {HF_API_TOKEN}"},
        data=audio_bytes.read(),
    )

    result = response.json()
    text = result.get("text", "Transcription failed.")
    return text
