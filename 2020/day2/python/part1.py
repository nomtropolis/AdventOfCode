from collections import Counter

INPUT_FILE = "../input.txt"

def is_valid(line):
    line_segments = line.split()
    how_many_min, how_many_max = [int(x) for x in line_segments[0].split("-")]
    char = line_segments[1][:-1]
    password_counts = Counter(line_segments[2])
    if password_counts[char] >= how_many_min and password_counts[char] <= how_many_max:
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
