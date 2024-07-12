#!/bin/bash

curl -X POST http://127.0.0.1:5000/api/timeline_post -d "name=Mark Fishbach&email=markiplier@youtube.com&content=Hello everyone my name is Markiplier."

curl http://127.0.0.1:5000/api/timeline_post

read -p "Press Enter to exit"