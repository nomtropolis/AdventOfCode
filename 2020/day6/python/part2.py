from collections import Counter

INPUT_FILE = "../input.txt"
# INPUT_FILE = "../input.example.txt"


def main():
    final_answer = 0
    group_members = 0
    group = Counter()

    with open(INPUT_FILE) as input_file:
        for line in input_file:
            if line == "\n":
                for answer, count in group.items():
                    if count == group_members:
                        final_answer += 1
                group.clear()
                group_members = 0
                continue
            group_members += 1
            for char in line:
                if char != "\n":
                    group.update(char)
    for answer, count in group.items():
        if count == group_members:
            final_answer += 1        
    print("The answer is {}".format(final_answer))

if __name__ == "__main__":
    main()
