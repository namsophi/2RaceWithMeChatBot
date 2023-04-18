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


with open('vids_regex.json') as f:
    debug_videos = json.load(f)

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

def get_videos(curr_state, text):
    while curr_state != SELECTION_FINISHED:
        if curr_state == INIT:
            print("chatbot: ", dialogues[curr_state]["expected_dialogue"])
            lst_vids = []
            while curr_state != SELECTION_FINISHED:
                print("user dialogue: ", text)
                if text != None:
                    for pattern, video in debug_videos.items():
                        if re.search(re.compile(pattern), text): 
                            # if a keyword matches, select the corresponding video from the dictionary
                            lst_vids.append(video) 
                    if len(lst_vids) == 0:
                        curr_state = CONFUSED
                        continue
                curr_state = SELECTION_FINISHED
                pprint(lst_vids)
                return lst_vids

get_videos(INIT, "a walk in the park")