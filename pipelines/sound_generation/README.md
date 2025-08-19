# Sound Generation Pipeline (Proof of Concept)

This directory contains proof-of-concept scripts for generating audio from text.

## Option 1: Lightweight TTS (Recommended for Quick Testing) - `generate_audio_lightweight.py`

This script provides a method for text-to-audio generation using the \`gTTS\` (Google Text-to-Speech) library, which leverages Google Translate's TTS API. It's less resource-intensive and serves as a reliable option for quick proof-of-concept audio generation, especially in environments with limited disk space or processing power.

### Model/Service Used:
- **Library**: \`gTTS\` (Python library)
- **Service**: Google Translate's Text-to-Speech API (requires an internet connection)

### Functionality:
1. Initializes the \`gTTS\` object with a given text prompt and language (defaulting to English).
2. Saves the generated speech as an \`.mp3\` file (e.g., \`lightweight_speech_gtts.mp3\`) in the script's directory.

### How to Run:
1. **Ensure Python is installed.**
2. **Install the necessary library**:
   The script attempts to install \`gTTS\` if it's not found. However, it's recommended to install it beforehand:
   \`\`\`bash
   pip install gTTS
   \`\`\`
3. **Run the script**:
   \`\`\`bash
   python pipelines/sound_generation/generate_audio_lightweight.py
   \`\`\`
   The script will connect to Google's TTS service to generate the audio.

### Output:
- A file named \`lightweight_speech_gtts.mp3\` will be created in the \`pipelines/sound_generation/\` directory.

### Note:
- This script requires an active internet connection.

---

## Option 2: Advanced TTS (Resource Intensive) - `generate_audio_hf.py`

This Python script demonstrates text-to-audio generation using the \`microsoft/speecht5_tts\` model along with the \`microsoft/speecht5_hifigan\` vocoder from Hugging Face Transformers.

**Note:** This script is resource-intensive (requires significant disk space for model downloads, e.g., PyTorch, and considerable memory/CPU for execution). It failed to run in some automated test environments due to these constraints. For a more reliable and less demanding option, see \`generate_audio_lightweight.py\`.

### Model Used:
- **Text-to-Speech Model**: \`microsoft/speecht5_tts\`
- **Vocoder**: \`microsoft/speecht5_hifigan\`
- **Speaker Embeddings**: From \`Matthijs/cmu-arctic-xvectors\` dataset.

### Functionality:
1. Initializes the SpeechT5 processor, TTS model, and HiFi-GAN vocoder.
2. Loads a predefined speaker embedding.
3. Takes a hardcoded text prompt.
4. Generates the corresponding speech audio.
5. Saves the generated audio as a \`.wav\` file named \`speech_poc.wav\`.

### How to Run:
1. **Ensure Python is installed.**
2. **Install necessary libraries**:
   The script attempts to install missing libraries. However, it's recommended to install them beforehand:
   \`\`\`bash
   pip install transformers datasets soundfile sentencepiece torch torchaudio
   \`\`\`
   You might also need to install \`libsndfile\` (e.g., \`sudo apt-get install libsndfile1\` on Debian/Ubuntu).
3. **Run the script**:
   \`\`\`bash
   python pipelines/sound_generation/generate_audio_hf.py
   \`\`\`
   The script will download large models from Hugging Face Hub on its first run.

### Output:
- A file named \`speech_poc.wav\` will be created in the \`pipelines/sound_generation/\` directory.

### Note:
This script serves as a PoC for using advanced Hugging Face models. Due to its resource requirements, its execution may be challenging in constrained environments.
