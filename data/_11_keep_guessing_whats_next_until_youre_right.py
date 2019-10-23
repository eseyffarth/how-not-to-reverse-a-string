# 11/20: Keep guessing what's next, until you're right

import random

def guess_and_consume_reverse(word):
    out = ""
    while word:
        next = random.randint(0, len(word)-1)
        if next == len(word) - 1:
            out += word[next]
            word = word[:next]
#             print("new word: {}".format(out))  # UNCOMMENT THIS!
#             print("old word: {}".format(word)) # UNCOMMENT THIS!
    return out

print(guess_and_consume_reverse("this is tedious"))