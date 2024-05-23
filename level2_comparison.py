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
Q_path = "Q.txt"
K_path = "K.txt"

q_words = get_words(Q_path)
q_freq = Counter(q_words).most_common()
k_words = get_words(K_path)
k_freq = Counter(k_words).most_common()
# Space between Q and K in display.
span = max(map(len, q_words))+9

print(f"Rank\tQ{str.join('', [' ']*span)}K")
i = 0
while True:
    for _ in range(20):
        if i >= max(len(q_freq), len(k_freq)):
            exit()
        q_len = len(q_freq[i][0])+7 if i<len(q_freq) else 1
        print(f" {i+1}\t{q_freq[i] if i<len(q_freq) else '-'}{str.join('', [' ']*(span-q_len))}{k_freq[i] if i < len(k_freq) else '-'}")
        i += 1
    input()