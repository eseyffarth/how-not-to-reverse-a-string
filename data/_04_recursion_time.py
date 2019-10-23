# 4/20: Recursion time!

def recursive_reverse(word):
    if len(word) == 1 or len(word) == 0:
#         print(word)   # UNCOMMENT FOR A FUN TIME!
        return word
    else:
#         print(word)   # UNCOMMENT FOR A FUN TIME!
        return "{}{}{}".format(word[-1], 
                               recursive_reverse(word[1:-1]), 
                               word[0])
    
print(recursive_reverse("almost a good solution!"))