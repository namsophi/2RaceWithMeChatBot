import json
import re

# clean the list of video json objects from videos.js
with open('vids_by_cat.json') as f:
    vids_cat = json.load(f)

def split_num_text(s): # helper function to split number and text
    head = s.rstrip('0123456789')
    return head.strip()

vids_organized = {}
vids_debug = {}
for (category, videos) in vids_cat.items():
    for video in videos:
        if video["vname"] == "PLEASE IGNORE":
            continue
        key_words = set() # use set to prevent duplicates
        if "tags" in video:  
            key_words.update(set(video["tags"]))
        key_words.update(set([video["type"]]))
        key_words.update(set([x.strip() for x in video["bilingualName"].split('/')])) # include bilingual video name
        # Note simply splitting by / is a rough division. Some names "Trails / Sentiers" work this way, some: "Xmas/Nöel City Hall Toronto" work less well
        key_words.update(set([x.strip() for x in category.split('/')])) # include bilingual category name
        key_words.update(set([video["vname"]]))
        key_words.update(set([x.strip() for x in video["vname"].split()]))
        keywords_without_number = [] # for videos like Algonquin 1, Algonquin 2, create new keyword without number called Algonquin
        new_key_words = set()
        for val in key_words:
            if split_num_text(val) not in keywords_without_number:
                keywords_without_number.append(split_num_text(val))
            # only keep words (Akihabara) or words + number (Akihabara 1). Remove single numbers (1)
            if not val.isnumeric():
                new_key_words.update(set([val]))
        new_key_words.update(set(keywords_without_number))
        # use regex to match keywords
        regex_keywords = []
         # use regex because it's faster to search through a list of keywords
        for val in new_key_words:
            regex_keywords.append('.*\\b'+val+'\\b.*')
        vid_key = '|'.join(regex_keywords)
        vids_organized[vid_key] = video
        video_debug = dict(video) # make a deep copy of video
        video_debug.pop("points")
        vids_debug[vid_key] = video_debug

with open("vids_new.json", "w") as outfile:
    json.dump(vids_organized, outfile, indent = 4, ensure_ascii=False)

with open("vids_debug.json", "w") as outfile:
    json.dump(vids_debug, outfile, indent = 4, ensure_ascii=False)