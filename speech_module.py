from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    file_path = "output.mp3"
    tts.save(file_path)

    # Open with default system player
    os.system(f"start {file_path}")