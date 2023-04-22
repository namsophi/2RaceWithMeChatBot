from utils import text_to_speech, listen, r, m
import json
import time
import speech_recognition as sr
import re
from pprint import pprint

# ENUMS for video selection script states
INIT = "init"
SELECTION_FINISHED = "selection_finished"

chatbot_init = "Hi, I'm Chatbot. What video would you like to select?"

with open('./video_parsing/vids_rev_index.json') as f:
    vids_rev_index = json.load(f)

def get_videos():
    text_to_speech(chatbot_init)
    print("chatbot: ", chatbot_init)
    lst_vids = []
    curr_state = INIT
    while curr_state != SELECTION_FINISHED:
        text = listen(r, m)
        print("user dialogue: ", text)
        if text != None:
            for term in text.split(' '):
                term = term.lower()
                if term in vids_rev_index:
                    videos = vids_rev_index[term]
                    lst_vids.extend(videos)
        result = list({v['vname']:v for v in lst_vids}.values()) # remove duplicate videos from multiple keywords
        curr_state = SELECTION_FINISHED
        print("result: ")
        for video in result:
            pprint(video)
        return result

get_videos()