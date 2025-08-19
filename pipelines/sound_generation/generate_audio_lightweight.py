from gtts import gTTS
import os

def generate_tts_audio(text_prompt, output_filename="generated_audio_gtts.mp3"):
    """
    Generates audio from a text prompt using gTTS and saves it as an .mp3 file.
    """
    print(f"Initializing gTTS with text: '{text_prompt}'")
    try:
        tts = gTTS(text=text_prompt, lang='en', slow=False)
        print("gTTS object created.")
    except Exception as e:
        print(f"Error initializing gTTS: {e}")
        print("This might be due to network issues or problems with the gTTS library itself.")
        return

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_filename)
    if output_dir and not os.path.exists(output_dir):
        print(f"Creating output directory: {output_dir}")
        os.makedirs(output_dir)
    elif not output_dir: # If output_filename is just a filename, output_dir will be empty
        print("Outputting to current directory.")


    print(f"Saving audio to {output_filename}...")
    try:
        tts.save(output_filename)
        print(f"Audio successfully saved to {output_filename}")
    except Exception as e:
        print(f"Error saving audio file with gTTS: {e}")
        print("Please check write permissions and if the filename is valid.")

if __name__ == "__main__":
    # Attempt to install gTTS if not present, for subtask environment
    try:
        import gtts
    except ImportError:
        print("gTTS library not found. Attempting to install...")
        try:
            # It's better to use subprocess for more control, but os.system is simpler for this PoC
            # and often sufficient if pip is in PATH.
            install_result = os.system("pip install gTTS")
            if install_result != 0:
                print(f"pip install gTTS failed with exit code {install_result}.")
                print("Please ensure pip is correctly configured and you have internet access.")
                print("ERROR_SCRIPT_WOULD_EXIT: gTTS installation failed.") # Replaced exit(1)
                # Skip further execution in this block if install failed
            else:
                print("gTTS installed successfully. You might need to re-run the script.")
                # Attempt to import again to be sure
            try:
                from gtts import gTTS # Re-assign to ensure it's the class, not the module
            except ImportError:
                print("Failed to import gTTS even after attempting installation. Exiting.")
                print("ERROR_SCRIPT_WOULD_EXIT: gTTS import failed after install.") # Replaced exit(1)
        except Exception as e:
            print(f"An error occurred during pip install: {e}")
            print("ERROR_SCRIPT_WOULD_EXIT: Exception during pip install.") # Replaced exit(1)

    # Conditional execution of the main logic based on successful import
    if 'gTTS' in locals() or 'gTTS' in globals():
        prompt = "Hello, this is a test of lightweight text to speech generation using the Google Text-to-Speech API via the gTTS library."

        # Save in the same directory as the script
        script_dir = os.path.dirname(__file__)
        # If script_dir is empty (e.g. script run from current dir), make it '.'
        if not script_dir:
            script_dir = "."
        output_path = os.path.join(script_dir, "lightweight_speech_gtts.mp3")

        print(f"Output path set to: {output_path}")
        generate_tts_audio(prompt, output_path)
        print("Lightweight TTS script finished.")
    else:
        print("Skipping audio generation because gTTS is not available.")
