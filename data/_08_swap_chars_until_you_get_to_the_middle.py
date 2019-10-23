# 8/20: Swap chars until you get to the middle

def swap_reverse(word):
    for i in range(len(word) // 2):
        start = word[:i] + word[-i-1]
        middle = word[i+1:-i-1]
        end = word[i] + int(bool(i)) * word[-i:]
        word = start + middle + end
#         print(word)     # UNCOMMENT FOR A FUN TIME!
    return word

print(swap_reverse("oof gimme a break"))