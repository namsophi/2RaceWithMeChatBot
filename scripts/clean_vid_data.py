import json
import re

# clean the list of video json objects from videos.js
with open('vids_not_nested.json') as f:
    all_videos = json.load(f)

def split_num_text(s): # helper function to split number and text
    head = s.rstrip('0123456789')
    return head.strip()

vids_organized = {}
# organize the vids_not_nested to use video name as key for faster indexing
for video in all_videos:
    key_words = []
    # use regex because it's faster to search through a list of keywords (video names and sub-components)
    video_vname = video["vname"]
    vid_bilingualName = video["bilingualName"]
    if '/' in vid_bilingualName: # include both french and english words as keywords
        result2 = [x.strip() for x in vid_bilingualName.split('/')]
        key_words.extend(result2)
    key_words.append(video_vname)
    key_words.append(vid_bilingualName)
    keywords_without_number = [] # for videos like Algonquin 1, Algonquin 2, create new keyword without number called Algonquin
    for i in range(len(key_words)):
        if split_num_text(key_words[i]) not in keywords_without_number:
            keywords_without_number.append(split_num_text(key_words[i]))
    key_words.extend(keywords_without_number)
    for i in range(len(key_words)):
        key_words[i] = '.*\\b'+key_words[i]+'\\b.*'
    vid_key = '|'.join(key_words)
    vids_organized[vid_key] = video

with open("vids_organized.json", "w") as outfile:
    json.dump(vids_organized, outfile, indent = 4)