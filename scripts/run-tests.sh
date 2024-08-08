#!/bin/bash

# Change to the parent directory (project root)
cd "$(dirname "$0")/.."

# Activate the virtual environment
source python3-virtualenv/bin/activate

# Run the tests
python -m unittest discover -v tests/