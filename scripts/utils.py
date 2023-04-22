from gtts import gTTS
import os
import speech_recognition as sr
import http.client as httplib
import ssl

r = sr.Recognizer()
m = sr.Microphone()

# helper function to check if internet is availableS
def have_internet():
    conn = httplib.HTTPSConnection("8.8.8.8", timeout=5, context = ssl._create_unverified_context())
    try:
        conn.request("HEAD", "/")
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        conn.close()

def listen(recognizer, microphone):
    with microphone as source:
        print("Listening...")
        audio = recognizer.listen(source)
        if have_internet() == True:
            try:
                text = recognizer.recognize_google(audio)
                print("You said : {}".format(text))
                return text
            except:
                print("Sorry, google speech to text could not recognize what you said")
                return None
        else:
            try:
                text = recognizer.recognize_sphinx(audio)
                print("You said : {}".format(text))
                return text
            except:
                print("Sorry, CMU sphinx could not recognize what you said")
                return None

def text_to_speech(text):
    # print("ai --> ", text)
    speaker = gTTS(text=text, lang="en", slow=False)
    speaker.save("res.mp3")
    os.system("afplay res.mp3")
    os.remove("res.mp3")

