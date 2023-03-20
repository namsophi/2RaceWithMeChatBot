import pyaudio
import speech_recognition as sr

# pa = pyaudio.PyAudio()
# print(pa.get_device_count())
# print(pa.get_default_input_device_info())


r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            return text
        except:
            print("Sorry could not recognize what you said")