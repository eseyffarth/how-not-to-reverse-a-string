# 3/20: Finally, some numpy!

import numpy as np     # oh là là that's fancy

def np_reverse(word):
    out = np.empty([len(word), len(word)], dtype=np.unicode_)
    out[0,] = np.asarray(list(word), dtype=np.unicode_)
#     print(out)    # UNCOMMENT FOR A FUN TIME!
    out = np.rot90(out)
#     print(out)    # UNCOMMENT FOR A FUN TIME!
    out = out.transpose(1,0)
#     print(out)    # UNCOMMENT FOR A FUN TIME!
    return "".join([c for c in out[0,]])

print(np_reverse("numpy is cool"))