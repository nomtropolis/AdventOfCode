# INPUT_FILE = "../input.example.txt"
INPUT_FILE = "../input.txt"


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
    jumps = []
    with open(INPUT_FILE) as input_file:
        line_count = 1
        for line in input_file:
            cmds[line_count] = line
            if "jmp" in line:
                jumps.append(line_count)
            line_count += 1
    return cmds, jumps


def try_get_through(cmds, override_position):
    acc = 0
    visited_positions = []
    previous_position = 1
    current_position = 1
    lowest_jump = 1
    while True:
        if current_position in cmds:
            cmd, movement, amt_to_add = handle_command(cmds[current_position])
        else:
            break
        if cmd == "jmp":
            # print("JUMP @ {}".format(current_position))
            if current_position > lowest_jump:
                lowest_jump = current_position
        if current_position == override_position:
            movement = 1
        next_position = current_position + movement
        acc += amt_to_add
        if next_position in visited_positions:
            return 0
        previous_position = current_position
        current_position = next_position
        visited_positions.append(current_position)
    print("Total accumulated: {}".format(acc))
    return 1

def main():
    cmds, jumps = build_cmd_list()
    for jump_position in jumps[::-1]:
        if try_get_through(cmds, jump_position):
            break

if __name__ == "__main__":
    main()
