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

# example data
with open('inv_index_example.json') as f:
    vids_rev_index = json.load(f)

# ## video data (to be improved)
# with open('vids_rev_index.json') as f:
#     vids_rev_index = json.load(f)

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
                            lst_vids.extend(vids_rev_index[term])
                curr_state = SELECTION_FINISHED
                if (len(lst_vids)) == 0: # no video was found, recommend the first video as default
                    lst_vids = vids_rev_index["park"]
                    pprint("Sorry, we could not recognize what you said or find corresponding videos.")
                    text_to_speech("Sorry, we could not find corresponding videos.")
                pprint(lst_vids)
                return lst_vids

get_videos(INIT)

# def get_videos_debug(curr_state, debug_text):
#     debug_text = debug_text.lower()
#     while curr_state != SELECTION_FINISHED:
#         if curr_state == INIT:
#             print("chatbot: ", dialogues[curr_state]["expected_dialogue"])
#             lst_vids = []
#             while curr_state != SELECTION_FINISHED:
#                 print("user dialogue: ", debug_text)
#                 if debug_text != None:
#                     for term in debug_text.split(' '):
#                         term = term.lower()
#                         if term in vids_rev_index:
#                             lst_vids.extend(vids_rev_index[term])
#                 curr_state = SELECTION_FINISHED
#                 pprint(lst_vids)
#                 return lst_vids

# get_videos_debug(INIT, "amusement park")