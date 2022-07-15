from gtts import gTTS
import os


def text_to_speech(text):
    print("ai --> ", text)
    speaker = gTTS(text=text, lang="en", slow=False)
    speaker.save("res.mp3")
    os.system("afplay res.mp3")
    os.remove("res.mp3")
