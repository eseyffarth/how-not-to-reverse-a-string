# 13/20: Make the user do the work... and suffer

import tkinter as tk
import random

word = input("Please enter the string you wish to reverse:\n>>> ")
print("Thank you. Please select the characters from the string " +
      "in their correct order.")
REV = ""

def place_label(canvas, label):
    if label["text"] != "DONE":
        label["command"] = lambda: add_clicked_char(label)
        
    # This part taken from https://stackoverflow.com/a/52526584
    '''place a label on a canvas in a random, 
    non-overlapping location'''
    width = label.winfo_reqwidth()
    height = label.winfo_reqheight()

    tries = 0
    while True and tries < 1000:
        tries += 1 # failsafe, to prevent an infinite loop
        x = random.randint(0, 200-width)
        y = random.randint(0, 200-height)
        items = canvas.find_overlapping(x, y, x+width, y+height)
        if len(items) == 0:
            canvas.create_window(x, y, window=label, anchor="nw")
            break

def add_clicked_char(label):
    global REV   # don't work with global variables, everyone
    REV += label["text"]
    label["state"] = "disabled"
    
def close():
    global REV  # don't work with global variables, everyone
    print("\nYou decided to reverse this string:\n'{}'\n".format(word) +
          "You selected this sequence to do so:\n'{}'\n\n".format(REV) +
          "Thank you for your time.")
    root.destroy()

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(fill="both", expand=True)

for c in word:
    label = tk.Button(root, 
                      text=c, 
                      font=('Helvetica', '20'))
    place_label(canvas, label)

exit = label = tk.Button(root, 
                         text="DONE", 
                         font=('Helvetica', '20'), 
                         command= close)
place_label(canvas, exit)

root.mainloop()