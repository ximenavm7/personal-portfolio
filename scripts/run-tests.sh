#!/bin/bash

# Change to the parent directory (project root)
cd /root/personal-portfolio

# Activate the virtual environment
#source python3-virtualenv/bin/activate

# Run the tests
python3-virtualenv/bin/python -m unittest discover -v tests/