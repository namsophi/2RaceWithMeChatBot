from utils import text_to_speech
import json
import time
import speech_recognition as sr
import re
from pprint import pprint

# ENUMS for video selection script states
INIT = "init"
SELECTION_FINISHED = "selection_finished"
CONFUSED = "confused"

with open('vids_rev_index.json') as f:
    vids_rev_index = json.load(f)

with open('video_select_script.json') as f:
    dialogues = json.load(f)

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

# Are you looking for video by country, province, state, or by title? Please use the keyword "country", "province", or "title" in your response 
# country:
# canada: Are you looking for general Canadian videos, or those of a specific province?
# general Canada: 3 general Canada videos
# specific province -> jump to province

# province: return corresponding videos based on videos.js

# did not find state

curr_state = INIT

final_res = {}
def get_videos(curr_state):
    while curr_state != SELECTION_FINISHED:
        if curr_state == INIT:
            text_to_speech(dialogues[curr_state]["expected_dialogue"])
            print("chatbot: ", dialogues[curr_state]["expected_dialogue"])
            lst_vids = []
            while curr_state != SELECTION_FINISHED:
                text = listen(r, m)
                print("user dialogue: ", text)
                if text != None:
                    for term in text.split(' '):
                        term = term.lower()
                        if term in vids_rev_index:
                            video = vids_rev_index[term]
                            video_view = video.items()

                            lst_vids.append(vids_rev_index[term])
                curr_state = SELECTION_FINISHED
                result = set.intersection(*[set(x) for x in lst_vids])  
                pprint("result", list(result))
                return result

get_videos(INIT)