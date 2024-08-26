#!/bin/bash

# Check if the file.txt exists
if [ ! -f "file.txt" ]; then
  echo "file.txt not found!"
  exit 1
fi

# Transpose the file content
awk '
BEGIN {
  # Read the file into an array
  while (getline > 0) {
    for (i = 1; i <= NF; i++) {
      matrix[NR, i] = $i
    }
    max_columns = NF
  }
}

# After reading the file, output the transposed matrix
END {
  for (i = 1; i <= max_columns; i++) {
    for (j = 1; j <= NR; j++) {
      if (j > 1) printf " "
      printf "%s", matrix[j, i]
    }
    print ""
  }
}
' file.txt
