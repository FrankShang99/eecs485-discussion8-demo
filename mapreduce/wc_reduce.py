import sys

words = {}
# Append all the words in the input files to dictionary of word-count pairs
for line in sys.stdin:
    split_line = line.rsplit()
    word = split_line[0]
    count = int(split_line[1])
    if word in words:
        # TODO: IMPLEMENT ME
    else:
        # TODO: IMPLEMENT ME

for key, val in words.items():
    # TODO: PRINT KEY-VALUE PAIRS
