#!/bin/bash

# kill existing tmux sessions
tmux kill-server

# move to portfolio project
cd /root/personal-portfolio

# update git repo
git fetch && git reset origin/main --hard

#install new dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt
deactivate

# Start a new detached tmux session and run the Flask server
tmux new-session -d -s portfolio
tmux send-keys -t portfolio "cd /root/personal-portfolio" C-m
tmux send-keys -t portfolio "source python3-virtualenv/bin/activate" C-m
tmux send-keys -t portfolio "flask run --host=0.0.0.0" C-m