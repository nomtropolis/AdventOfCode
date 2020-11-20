from functools import reduce

INPUT_FILE="../input.txt"

def main():
    total_ribbon = 0
    with open(INPUT_FILE) as input_file:
        for dimensions in input_file:
            sides = [int(x) for x in dimensions.split('x')]
            bow = reduce(lambda x, y: x * y, sides, 1)
            sides.remove(max(sides))
            package_ribbon = sum(sides) * 2
            total_ribbon += (package_ribbon + bow)
    print("Total Ribbon: {}".format(total_ribbon))

if __name__ == "__main__":
    main()
