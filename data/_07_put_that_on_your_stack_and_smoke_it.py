# 7/20: Put that on your stack and smoke it

class Stack_Reverser():
    def __init__(self, input_word):
        self.original_word = input_word
        self.stack = []
        
    def is_empty(self):
        return not bool(len(self.stack))
    
    def add_element(self, el):
        self.stack.append(el)
        
    def remove_element(self):
        return self.stack.pop()
    
    def reverse_string(self):
        out = ""
        for c in self.original_word:
            self.add_element(c)
#         print(self.stack)   # UNCOMMENT FOR A FUN TIME!
        while not self.is_empty():
            out += self.remove_element()
#             print(out)      # UNCOMMENT FOR A FUN TIME!
        return out
    
lfs = Stack_Reverser("now that's what I call professional.")
print(lfs.reverse_string())