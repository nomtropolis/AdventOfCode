from collections import Counter

INPUT_FILE = "../input.txt"

def has_bad_strings(word):
    bad_strings = ["ab", "cd", "pq", "xy"]
    for bad_string in bad_strings:
        if bad_string in word:
            return True
    return False

def has_repeated_char(word):
    current_char = ""
    for char in word:
        if char == current_char:
            return True
        current_char = char
    return False

def has_three_vowels(word):
    vowels = "aeiou"
    vowel_count = 0
    for char in word:
        if char in vowels:
            vowel_count += 1
            if vowel_count > 2:
                return True
    return False

def is_naughty(word):
    if has_bad_strings(word):
        return True
    if not has_repeated_char(word):
        return True
    if not has_three_vowels(word):
        return True
    return False

def main():
    nice_strings = 0
    with open(INPUT_FILE) as input_file:
        for line in input_file:
            line = line.replace("\n", "")
            print("Checking {}".format(line))
            if is_naughty(line):
                continue
            print("{} is Nice!".format(line))
            nice_strings += 1
    print("There are {} nice strings.".format(nice_strings))

if __name__ == "__main__":
    main()
