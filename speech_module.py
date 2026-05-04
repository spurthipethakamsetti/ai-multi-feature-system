from gtts import gTTS

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    file_path = "output.mp3"
    tts.save(file_path)
    return file_path   # return file instead of playing
