# 6/20: Pop random chars and insert (at correct indices)

import random

def pop_reverse(word):
    out = [None] * len(word)
#     print(out)        # UNCOMMENT FOR A FUN TIME!
    while None in out:
        next_char_pos = random.randint(0, len(word)-1)
        out[-next_char_pos-1] = word[next_char_pos]
#         print(out)    # UNCOMMENT FOR A FUN TIME!
    return "".join(out)

print(pop_reverse("why would anyone do this??"))