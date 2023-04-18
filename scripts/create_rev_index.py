import json
import re

punctuation = "!@#$%^&*()_+<>?:.,;-/"  # for removing punctuation
stopwords = ["a", "an", "the"]

# clean the list of video json objects from videos.js
with open('vids_by_cat.json') as f:
    vids_cat = json.load(f)

def split_num_text(s): # helper function to split number and text by removing trailing numbers
    head = s.rstrip('0123456789')
    return head.strip()

vids_organized = {}
vids_rev_index = {}
for (category, videos) in vids_cat.items():
    for video in videos:
        if video["vname"] == "PLEASE IGNORE":
            continue
        keywords = set() # use set to prevent duplicates
        keywords.update(set([x.strip() for x in category.split('/')])) # include bilingual category name
        keywords.update(set([video["vname"]]))
        keywords.update(set([x.strip() for x in video["vname"].split()])) # gets individual words in a video
        
        # Note simply splitting by / is a rough division. Some names "Trails / Sentiers" work this way, some: "Xmas/Nöel City Hall Toronto" work less well
        keywords.update(set([x.strip() for x in video["bilingualName"].split('/')])) # include bilingual video name
        keywords.update(set([video["type"]])) # add type to keywords
        if "tags" in video:  
            keywords.update(set(video["tags"])) # add tags to keywords
        # new_keywords set for final cleaning
        new_keywords = set()
        for val in keywords:
            # only keep words (Akihabara) or words + number (Akihabara 1). Remove single numbers (1)
            # if not val.isnumeric():
            val = val.strip(punctuation)
            val = val.lower()
            # for videos like Distillery Christmas 1, create new keyword without number called Distillery Christmas
            new_keywords.update(set([split_num_text(val)]))
            new_keywords.update(set([val]))
        
        # make a copy of video without the points, easier to see for debugging purposes whether data is parsed correctly
        video_debug = dict(video) # make a deep copy of video
        video_debug.pop("points")

        # for each word in new_keywords, make it into a key, then add curr video to list of videos indexed by key
        for val in new_keywords:
            if val == "" or val.isnumeric() or len(val) == 1: # don't keep empty string or string of just number "1"
                continue
            for stopword in stopwords:
                if val == stopword:
                    continue
            if val not in vids_rev_index:
                vids_rev_index[val] = [video_debug]
            else:
                vids_rev_index[val].append(video_debug)
        
        # sort the new dictionary
        vids_sorted = dict(sorted(vids_rev_index.items()))

# with open("vids_new.json", "w") as outfile:
#     json.dump(vids_organized, outfile, indent = 4, ensure_ascii=False)

with open("vids_rev_index.json", "w") as outfile:
    json.dump(vids_sorted, outfile, indent = 4, ensure_ascii=False)