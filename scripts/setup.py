from utils import text_to_speech
import json
import time
import speech_recognition as sr

with open('setup_script.json') as f:
   dialogues = json.load(f)

num_dialogues = len(dialogues)
curr_state = 0

r = sr.Recognizer()
m = sr.Microphone()

def listen(recognizer, microphone):
    with microphone as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said : {}".format(text))
            return text
        except:
            print("Sorry could not recognize what you said")
            return None
    return None

while curr_state < num_dialogues:
    if dialogues[curr_state]["speaker"] == "user":
        while True:
            text = listen(r, m)
            print("text: ", text)
            if text != None:
                print("keyword: ", dialogues[curr_state]["keyword"].lower())
                if dialogues[curr_state]["keyword"].lower() in text.lower():
                    curr_state += 1
                break
    elif dialogues[curr_state]["speaker"] == "chatbot":
        text_to_speech(dialogues[curr_state]["expected_dialogue"])
        print(dialogues[curr_state]["expected_dialogue"])
        curr_state += 1

