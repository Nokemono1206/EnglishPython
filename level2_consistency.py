import re
from collections import Counter

# Read file and return a list of words in the file.
def get_words(filepath) -> list:
    with open(filepath) as f:
        words = f.read()
        words = re.split("[.,\s]", words)
        words = [x for x in words if x]
        return words

# path of Q and K texts.
filepaths = ["Q.txt", "K.txt", "test.txt"]

counters = [Counter(get_words(f)) for f in filepaths]
total = Counter()
for c in counters:
    total += c
total = total.most_common()
dictionaries = [dict(c) for c in counters]
max_words_len = 15

# Space between Q and K in display.
sep = "    "

print(f"Words{' '*(max_words_len-5)+str.join(' ', filepaths)}")
i = 0
while True:
    for _ in range(20):
        if i >= len(total):
            exit()
        print(total[i][0]+(" "*(max_words_len-len(total[i][0]))),
                *["-" if total[i][0] not in d else d[total[i][0]] for d in dictionaries],
                sep=sep)
        i += 1
    input()