# 14/20: Make the user suffer, but be polite about it

import random

# Idea by @Mattlaschneider on Twitter

def ask_reverse(word):
    out = ""
    while len(out) < len(word):
        next = random.randint(0, len(word)-1)
        is_this_it = input(("You entered this word: \t{}\n" +
                           "Our output so far is this:\t{}\n" +
                           "Should I add this char (y/n)?\t{}\n>>> ").
                           format(word, out, word[next]))
        if is_this_it.lower() in ["yes", "y"]:
            out += word[next]
    return "Here is your result:\t{}".format(out)

print(ask_reverse("Matt"))