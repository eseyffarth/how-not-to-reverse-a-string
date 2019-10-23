# 12/20: Introduce a human to the task!

def learn_reverse():
    known_reverses = {}
    w = input("What would you like to reverse?\n> ")
    while w:
        if w in known_reverses:
            print("The reverse of '{}' is '{}'.".format(w, 
                                                known_reverses[w]))
        else:
            t = input("Sorry, I don't know that string. " +
                      "Please tell me how to reverse it.\n> ")
            if not t:
                break
            known_reverses[w] = t
        w = input("What would you like to reverse now?\n> ")
    print("Goodbye! Thank you for teaching me!")
    
learn_reverse()