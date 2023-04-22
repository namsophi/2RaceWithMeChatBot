# 2RaceWithMeChatBot

This is the backend repository for the 2RaceWithMe Chatbot 

## To run backend server  

1) run `git clone git@github.com:namsophi/2RaceWithMeChatBot.git` in a terminal window
2) navigate into the project
3) (Optional) set up a virtual environment (venv or conda)
4) run `pip install -r requirements.txt` to download the required libraries for the project
5) run `flask run`

## To run setup

1) `cd scripts` to cd into scripts directory
2) `python setup.py` to run the setup script
3) Call chatbot to start setting up with the keyword "chatbot"
4) follow chatbot instructions to setup

## To run video selection

1) video_parsing folder is for parsing the 2RaceWithMe video objects into keywords since they are currently untagged.
2) to run video parsing process, cd into the folder, then `node videos.js` and `python create_rev_index.py`
3) if videos are already parsed, now `cd scripts` and run `python video_selection.py`