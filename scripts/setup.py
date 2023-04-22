from utils import text_to_speech, listen, r, m
import json
import http.client as httplib
import ssl

with open('./setup_script/setup_script.json') as f:
   dialogues = json.load(f)

num_dialogues = len(dialogues)
curr_state = 0

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

