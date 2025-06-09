#!/bin/bash

alias py="python3"

# activate virtual environment from current directory if not already activated
if [ -d "./venv" ]; then
    # Check if VIRTUAL_ENV points to ./venv
    if [ "$VIRTUAL_ENV" != "$(pwd)/venv" ]; then
        source ./venv/bin/activate
        pip3 install -r requirements.txt > /dev/null 2>&1 || echo "Error installing requirements."
    
    fi
else
    echo "virtual environment ./venv not found. better create one."
    exit 1
fi

function get_cs50_code() {
    # Check if the CS50 code is provided as an argument
    if [ -z "$1" ]; then
        echo "Example: get_cs50_code https://cs50.harvard.edu/ai/2024/projects/0/degrees/degrees.zip"
        return 1
    fi

    # Extract the filename from the URL (everything after the last '/')
    local zip_file="${1##*/}"

    # Download the zip file
    curl -L -o "$zip_file" "$1" &&

    # Unzip the file
    unzip -o "$zip_file" && 

    # Delete the original zip file
    rm -f "$zip_file"  && 

    # print the folder name that was created without .zip extension
    echo &&
    echo "downloaded: ${zip_file%.zip}/" 
    echo
}

# NOTES 
# view CS50 AI - https://cs50.harvard.edu/ai/2024/projects/0/degrees/