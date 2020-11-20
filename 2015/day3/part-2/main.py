# INPUT_FILE = "../examples/input.robo-example1.txt"
# INPUT_FILE = "../examples/input.example2.txt"
# INPUT_FILE = "../examples/input.example3.txt"
INPUT_FILE = "../input.txt"

class Deliverer(object):
    def __init__(self, name, start_location):
        self.name = name
        self.location = start_location

    def __str__(self):
        return "{} - {}".format(self.name, self.location)

    @staticmethod
    def interpret_command(cmd):
        if cmd in ("", "\n"):
            return (0, 0)
        elif cmd == ">":
            return (1, 0)
        elif cmd == "<":
            return (-1, 0)
        elif cmd == "^":
            return (0, 1)
        elif cmd == "v":
            return (0, -1)

    def move(self, cmd):
        direction = Deliverer.interpret_command(cmd)
        new_location = (
            (self.location[0] + direction[0]),
            (self.location[1] + direction[1])
        )
        print("{} moves to {}".format(self, new_location))
        self.location = new_location

def main():
    visited_houses = 1
    start_position = (0, 0)
    locations = [start_position, ]

    santa = Deliverer("santa", start_position)
    robot = Deliverer("robot", start_position)

    with open(INPUT_FILE) as input_file:
        for line in input_file:
            char_num = 1
            for char in line:
                if char_num % 2 == 0:
                    mover = robot
                else:
                    mover = santa
                mover.move(char)
                if mover.location not in locations:
                    locations.append(mover.location)
                    visited_houses += 1
                char_num += 1
    print("\nTotal unique visits: {}".format(visited_houses))

if __name__ == "__main__":
    main()
