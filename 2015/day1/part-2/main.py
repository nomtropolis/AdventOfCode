INPUT_FILE="../input.txt"


def main():
    char_num = 0
    floor = 0
    with open(INPUT_FILE) as aoc_file:
        for line in aoc_file:
            for char in line:
                char_num += 1
                if char == "(":
                    floor += 1
                elif char == ")":
                    floor -= 1
                elif char == "":
                    continue
                elif char == "\n":
                    continue
                else:
                    print("Unexpected Value: '{}'".format(char))
                    exit(-1)
                if floor < 0:
                    print("Entered basement at position: {}".format(char_num))
                    exit(0)
    print("Floor: {}".format(floor))


if __name__ == "__main__":
    main()
