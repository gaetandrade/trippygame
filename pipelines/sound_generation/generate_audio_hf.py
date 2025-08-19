import torch
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import soundfile as sf
import os

def generate_audio(text_prompt, output_filename="generated_audio.wav"):
    """
    Generates audio from a text prompt using SpeechT5 and saves it as a .wav file.
    """
    print("Initializing models and processor...")
    try:
        # Load processor and model
        # Using a well-established TTS model for reliability in PoC
        processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
        model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
        vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
    except Exception as e:
        print(f"Error loading SpeechT5 models: {e}")
        print("Please ensure you have an active internet connection and the Hugging Face model repository is accessible.")
        return

    print("Models and processor loaded.")

    print(f"Processing text prompt: '{text_prompt}'")
    inputs = processor(text=text_prompt, return_tensors="pt")

    # Load xvector containing speaker's voice characteristics from a dataset
    # (This is required for SpeechT5)
    print("Loading speaker embeddings...")
    try:
        embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
        # Using a specific speaker embedding for reproducibility
        speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
    except Exception as e:
        print(f"Error loading speaker embeddings: {e}")
        print("Please ensure you have an active internet connection and the Hugging Face dataset is accessible.")
        return

    print("Speaker embeddings loaded.")

    print("Generating speech...")
    try:
        with torch.no_grad(): # Ensure no gradients are computed during inference
            speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)
    except Exception as e:
        print(f"Error during speech generation: {e}")
        return

    print("Speech generated.")

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the audio file
    try:
        sf.write(output_filename, speech.cpu().numpy(), samplerate=16000)
        print(f"Audio saved to {output_filename}")
    except Exception as e:
        print(f"Error saving audio file: {e}")

if __name__ == "__main__":
    # Install necessary libraries if they are not present
    # This is for ease of execution in the subtask environment
    try:
        import transformers
        import datasets
        import soundfile
        import sentencepiece # Often a dependency for tokenizers
    except ImportError:
        print("Attempting to install missing libraries: transformers, datasets, soundfile, sentencepiece, torch")
        os.system("pip install transformers datasets soundfile sentencepiece torch")
        print("Installation complete. Please re-run the script if it was interrupted.")
        # Re-check to ensure pip install worked before proceeding
        try:
            import transformers
            import datasets
            import soundfile
            import sentencepiece
        except ImportError:
            print("Failed to install necessary libraries. Please install them manually and try again.")
            exit(1)


    prompt = "Hello, this is a test of text to speech generation using Hugging Face transformers."
    # Save in the same directory as the script
    script_dir = os.path.dirname(__file__)
    output_path = os.path.join(script_dir, "speech_poc.wav")

    print(f"Output path set to: {output_path}")
    generate_audio(prompt, output_path)
    print("Proof of concept script finished.")
