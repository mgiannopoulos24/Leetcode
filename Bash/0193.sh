#!/bin/bash

# Check if the file file.txt exists
if [ ! -f "file.txt" ]; then
    echo "File file.txt not found!"
    exit 1
fi

# Filter and print valid phone numbers
grep -E '^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$|^[0-9]{3}-[0-9]{3}-[0-9]{4}$' file.txt
