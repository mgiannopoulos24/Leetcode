#!/bin/bash
# Check if the file exists
if [[ -f file.txt ]]; then
  # Print the 10th line of the file
  sed -n '10p' file.txt
else
  echo "file.txt does not exist."
fi
