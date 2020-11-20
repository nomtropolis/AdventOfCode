# INPUT_FILE = "../examples/input.example1.txt"
# INPUT_FILE = "../examples/input.example2.txt"
# INPUT_FILE = "../examples/input.example3.txt"
INPUT_FILE = "../input.txt"

def get_direction(symbol):
    if symbol in ("", "\n"):
        return (0, 0)
    elif symbol == ">":
        return (1, 0)
    elif symbol == "<":
        return (-1, 0)
    elif symbol == "^":
        return (0, 1)
    elif symbol == "v":
        return (0, -1)

def main():
    visited_houses = 1
    current_position = (0, 0)
    locations = [current_position, ]

    with open(INPUT_FILE) as input_file:
        for line in input_file:
            for char in line:
                print("==================================================")
                direction = get_direction(char)
                new_position = (
                    (current_position[0] + direction[0]),
                    (current_position[1] + direction[1])
                )
                print("Moving {} + {} -> {}".format(current_position, direction, new_position))
                current_position = new_position
                if current_position not in locations:
                    locations.append(current_position)
                    visited_houses += 1
    print("\nTotal unique visits: {}".format(visited_houses))

if __name__ == "__main__":
    main()
