# 16/20: Sleep on it!

# original code from 
# https://twitter.com/miseryconfusion/status/1091052050085888006

import time
import sys
from threading import Thread

def sleep_append(delay, el, output):
    delay = delay/5  # change the number to set the speed
    time.sleep(delay)
#     print(output)     # UNCOMMENT FOR A FUN TIME!
    output.append(el)
    
def sleep_reverse(l):
    output = []
    threads = [Thread(target=sleep_append, 
                      args=(len(l)-i, v, output)) \
               for i, v in enumerate(l)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return ''.join(output)

print(sleep_reverse("@miseryconfusion"))