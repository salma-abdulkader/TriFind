import gradio as gr
import IPython.display as ipd
from models.clip_model import model, processor, tokenizer, device
from models.faiss_index import index, image_paths
from models.whisper_api import transcribe_speech
from models.sentiment_feedback import submit_feedback_fn
from models.tts_model import text_to_speech
from app.config import IMAGE_DIR

print("Launching Gradio Interface...")

if model is not None and processor is not None and tokenizer is not None and index is not None and image_paths is not None:
    from models.faiss_index import multimodal_search_interface

    with gr.Blocks() as iface:
        gr.Markdown(
            """
            # Multimodal Product Search
            Search for products using text, image, or speech. Ensure you have placed images in the 'data_images' directory for indexing before running the search.
            """
        )
           
        with gr.Row():
            text_input = gr.Textbox(label="Text Query (Optional)", scale=2)
            audio_input = gr.Audio(sources=["microphone"], type="numpy", label="Record Audio Query (Optional)", scale=1)

        image_input = gr.Image(type="filepath", label="Upload Image Query (Optional)", height=300)
        search_button = gr.Button("Search")
        transcribed_text_output = gr.Textbox(label="Transcribed Speech", interactive=False)
        gallery_output = gr.Gallery(label="Search Results", columns=3, rows=3, object_fit="contain", height=400)
        
        # Welcome message (TTS)
        welcome_audio = text_to_speech("Welcome to the product search system.")
        if welcome_audio:
            display(ipd.Audio(welcome_audio, autoplay=True))
            
        search_button.click(
            fn=multimodal_search_interface,
            inputs=[text_input, image_input, audio_input],
            outputs=[gallery_output, transcribed_text_output])

        # Feedback Section
        gr.Markdown("---")
        gr.Markdown("### 📝 Feedback Section")

        with gr.Row():
            feedback_text = gr.Textbox(
                label="Write your feedback here",
                placeholder="Share your thoughts about your experience...",
                lines=4,
                scale=2
            )
            rating = gr.Slider(
                minimum=1,
                maximum=5,
                step=1,
                label="Rating (1–5 ⭐)",
                value=5,
                scale=1
            )

        submit_feedback = gr.Button("Submit Feedback")
        feedback_output = gr.Textbox(label="Status", interactive=False)

        submit_feedback.click(
            fn=submit_feedback_fn,
            inputs=[text_input, audio_input, image_input, transcribed_text_output, feedback_text, rating],
            outputs=[feedback_output]
        )

    iface.launch(share=True, debug=True)
else:
    print("Cannot launch Gradio interface. Essential components are not loaded. Please check the setup steps.")
