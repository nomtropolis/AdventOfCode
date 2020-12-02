from collections import Counter

INPUT_FILE = "../input.txt"

def is_valid(line):
    line_segments = line.split()
    position1, position2 = [int(x)-1 for x in line_segments[0].split("-")]
    char = line_segments[1][:-1]
    password = line_segments[2]
    if password[position1] == password[position2]:
        return False
    if password[position1] == char or password[position2] == char:
        return True
    return False

def main():
    valid_passwords = 0
    with open(INPUT_FILE) as input_file:
        for line in input_file:
            if is_valid(line):
                valid_passwords += 1
    print(valid_passwords)

if __name__ == "__main__":
    main()
