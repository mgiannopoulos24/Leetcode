#!/bin/bash

# Check if the file words.txt exists
if [ ! -f "words.txt" ]; then
    echo "File words.txt not found!"
    exit 1
fi

# Calculate the frequency of each word and sort by descending frequency
cat words.txt | \
tr -s ' ' '\n' | \
grep -v '^$' | \
sort | \
uniq -c | \
sort -nr | \
awk '{print $2, $1}'
