# 2/20: Switch it up

def both_sides_reverse(word):
    word = list(word)
    for i in range(len(word)):
#         print("".join(word))   # UNCOMMENT FOR A FUN TIME!
        new_i = len(word) - i-1
        for j in range(0, new_i):
            word[j], word[j+1] = word[j+1], word[j]
    return "".join(word)

print(both_sides_reverse("swappity swap"))