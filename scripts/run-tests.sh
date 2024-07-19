#!/bin/bash

# Change to root directory
cd ..

# Execute "unittest" command to run tests in "tests" folder
python3-virtualenv/bin/python -m unittest discover -v tests/