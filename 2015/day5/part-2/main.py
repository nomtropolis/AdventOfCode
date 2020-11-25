from collections import Counter
from pprint import pprint

INPUT_FILE = "../input.txt"

def is_naughty(word):
    print("Working on: {}".format(word))
    has_repeating_pair = False
    has_alternating_chars = False
    for i, char in enumerate(word):
        if i > 0 and i < len(word) - 1:
            if word[i-1] + word[i] in word[i+1:]:
                has_repeating_pair = True
        if i > 1:
            if word[i] == word[i-2]:
                has_alternating_chars = True
        if has_repeating_pair and has_alternating_chars:
            return False
    return True

def main():
    nice_strings = 0
    with open(INPUT_FILE) as input_file:
        for line in input_file:
            line = line.replace("\n", "")
            if is_naughty(line):
                continue
            nice_strings += 1
    print("There are {} nice strings.".format(nice_strings))

if __name__ == "__main__":
    main()
