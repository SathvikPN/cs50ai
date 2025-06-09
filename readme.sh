#!/bin/bash

alias py="python3"

# activate virtual environment from current directory if not already activated
if [ -d "./venv" ]; then
    # Check if VIRTUAL_ENV points to ./venv
    if [ "$VIRTUAL_ENV" != "$(pwd)/venv" ]; then
        source ./venv/bin/activate && 
        pip3 install -r requirements.txt
    fi
else
    echo "virtual environment ./venv not found. better create one."
    exit 1
fi

# NOTES 
# view CS50 AI - https://cs50.harvard.edu/ai/2024/projects/0/degrees/