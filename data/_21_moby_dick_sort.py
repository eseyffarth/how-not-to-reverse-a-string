# 21/20: Moby Dick, or kciD yboM

import urllib.request

SOURCE_URL = "https://www.gutenberg.org/cache/epub/2489/pg2489.txt"


def moby_sort(string):

    # Download Moby Dick
    data = urllib.request.urlopen(SOURCE_URL)

    # We'll start from the end of the input string
    todo = len(string) - 1
    found = ""

    # Convert all lines from bytes to string, strip newlines
    lines = [str(line.strip()) for line in data]

    # Go through each line in the book, backwards (could just as well go forwards)
    for line in reversed(lines):

        # Is the character we want in this line?
        # Do we still have characters to find?
        pos = line.find(string[todo])
        if pos != -1 and todo >= 0:
            # It is! We do! Grab it!
            found += line[pos]
            todo -= 1

        # Even if we've found the full string, keep iterating through all the lines.
        # It's a good book, the computer might enjoy it (backwards).

    return found


print(moby_sort("Hermann Melville"))
