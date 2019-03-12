import sys

words = {}
# Append all the words in the input files to dictionary of word-count pairs
for line in sys.stdin:
    split_line = line.rsplit()
    word = split_line[0]
    count = int(split_line[1])
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

for key, val in words.items():
    print('{}\t{}'.format(key, val))
