INPUT_FILE = "../input.example.txt"
# INPUT_FILE = "../input.txt"

def handle_command(cmd):
    action, signed_digit = cmd.split(" ")
    if action == "nop":
        return "nop", 1, 0
    elif action == "acc":
        return "acc", 1, int(signed_digit)
    elif action == "jmp":
        return "jmp", int(signed_digit), 0

def build_cmd_list():
    cmds = {}
    with open(INPUT_FILE) as input_file:
        line_count = 0
        for line in input_file:
            cmds[line_count] = line
            line_count += 1
    return cmds

def main():
    cmds = build_cmd_list()

    acc = 0
    visited_positions = []
    previous_position = 0
    current_position = 0
    while True:
        cmd, movement, amt_to_add = handle_command(cmds[current_position])
        next_position = current_position + movement
        acc += amt_to_add
        if next_position in visited_positions:
            print("Next move is duplicate: \n\tPrevious_postion: {}\n\tcurrent_position: {}\n\tnext_position: {}".format(previous_position, current_position, next_position))
            break
        previous_position = current_position
        current_position = next_position
        visited_positions.append(current_position)
        print("New_position: {}".format(current_position))
    print("Total accumulated: {}".format(acc))

if __name__ == "__main__":
    main()
