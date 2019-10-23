# 15/20: Look it up via an API!
# - STEP 2 OF 2 -

# And now, let's talk to the server!
# Query the reverse-string API and return the value found 
# for the input string.

import requests
import json

def api_reverse(w):
    try:
        r = requests.get('http://localhost:5000/{}'.format(w)).json()
        return r[w]
    except Exception as e:
        # whoops, probably forgot to start the API first
        print("Can't get the answer, maybe the API isn't running?")
        print("\nFull error description:{}".format(e))
        return
        

print(api_reverse("enjoy"))

print(api_reverse("item that is not found on the pre-defined list"))