from functools import reduce
import operator

INPUT_FILE="../input.txt"

def print_location(line, position, skip_rows):
    if skip_rows:
        print(line)
    else:
        print("{}[{}]{}".format(
            line[:position[0]],
            line[position[0]],
            line[position[0]+1:]
        ))


def main():
    slopes = [[1, -1], [3, -1], [5, -1], [7, -1], [1, -2]]

    line_count = 0
    tree_encounters = 0
    skip_rows = 0

    slope_encounter_counts = {}

    for slope in slopes:
        position = [0, 0]
        line_count = 0
        print("On slope: {}".format(slope))
        with open(INPUT_FILE) as input_file:
            for line in input_file:
                line = line.replace('\n', "")
                line_count += 1

                # `skip_rows` would have been set in a previous iteration,
                # if slope had you going down more than one row at a time.
                # just print a blank row / no encouter (skip it).
                if skip_rows:
                    print(line)
                    skip_rows -= 1 # we may have more rows to skip
                    continue

                print_location(line, position, skip_rows)

                encounter = line[position[0]]
                print("Encounter = {}".format(encounter))
                if encounter == "#":
                    slope_encounter_counts.setdefault(str(slope), 0)
                    slope_encounter_counts[str(slope)] += 1

                # update to new position
                position[0] = position[0] + slope[0]
                if position[0] >= len(line):
                    position[0] = position[0] - (len(line))

                # skip some rows if we have a steep slope
                if slope[1] < -1: # normal is -1, if we're more, skip N
                    skip_rows = abs(slope[1]) - 1
        print("=====================================================")
        print(slope_encounter_counts)
    print("Trees Encountered per slope multiplied: {}".format(reduce(operator.mul, slope_encounter_counts.values(), 1)))

if __name__ == "__main__":
    main()
