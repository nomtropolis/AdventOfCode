INPUT_FILE="../input.txt"

# note this assumes slope with a position once on each line

def main():
    start = [0, 0]
    position = start
    slope = [3, -1]
    line_count = 0
    trees = 0

    with open(INPUT_FILE) as input_file:
        for line in input_file:
            line = line.replace('\n', "")
            if line_count == 0:
                print(line)
                line_count += 1
                continue
            
            new_location = position[0] + slope[0]
            if new_location >= (len(line)):
                new_location = new_location - len(line)
            if line and line[new_location]:
                encounter = line[new_location]
            else:
                print("line: {}, new_location: {}".format(line, new_location))
            print("{}[{}]{}".format(
                line[:new_location],
                line[new_location:new_location+1],
                line[new_location+1:]
            ))
            line_count += 1
            position[0] = new_location
            if encounter == "#":
                trees += 1
    print("Trees: {}".format(trees))

if __name__ == "__main__":
    print("Starting")
    main()
