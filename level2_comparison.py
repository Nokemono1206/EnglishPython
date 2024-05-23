import re

# Read file and create a dictionary of {"word", "count"}.
def get_words(filepath) -> dict:
    with open(filepath) as f:
        words = f.read()
        words = re.split("[.,\s]", words)
        result = dict()
        for w in words:
            if not w:
                continue
            if w in result.keys():
                result[w] = result[w]+1
            else:
                result[w] = 1
        return result

# path of Q and K texts.
Q_path = "Q.txt"
K_path = "K.txt"

q_words = get_words(Q_path)
q_freq = sorted(q_words.items(), key=lambda x: x[1], reverse=True)
k_words = get_words(K_path)
k_freq = sorted(k_words.items(), key=lambda x: x[1], reverse=True)
# Space between Q and K in display.
span = max(map(len, q_words.keys()))+9

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