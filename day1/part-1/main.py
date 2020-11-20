INPUT_FILE="../input.txt"


def main():
    floor = 0
    with open(INPUT_FILE) as aoc_file:
        for line in aoc_file:
            for char in line:
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
    print("Floor: {}".format(floor))


if __name__ == "__main__":
    main()
