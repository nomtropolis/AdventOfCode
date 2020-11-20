from hashlib import md5
import sys

PUZZLE_INPUT="ckczppom"
counter = 1

if len(sys.argv) == 1:
    LEADING_DIGITS = "0000"
else:
    LEADING_DIGITS = "0"*int(sys.argv[1])
    
while True:
    if counter % 100 == 0:
        print("On digit: {}".format(counter))

    thing = md5("{}{}".format(PUZZLE_INPUT, counter).encode("UTF-8")).hexdigest()

    if thing.startswith(LEADING_DIGITS):
        print("Found: {}".format(counter))
        break

    counter += 1
