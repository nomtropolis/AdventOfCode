from collections import Counter
import re

# INPUT_FILE = "input2.txt"
# GRID_SIZE_X = 1000
# GRID_SIZE_Y = 1000


# INPUT_FILE = "input3.txt"
# GRID_SIZE_X = 10
# GRID_SIZE_Y = 10

INPUT_FILE = "input.txt"
GRID_SIZE_X = 1000
GRID_SIZE_Y = 1000


def build_initial_light_matrix():
    light_matrix = []
    for x in range(0,GRID_SIZE_X):
        light_matrix.append([])
        for y in range(0, GRID_SIZE_Y):
            light_matrix[x].append("0")
    return light_matrix

def count_lights(light_matrix):
    light_string = ""
    for x in light_matrix:
        for y in x:
            light_string += y
    # lights = Counter("".join("".join(light_matrix))
    print(light_string)
    lights = Counter(light_string)
    return lights["1"]

def set_value(light_matrix, position, value):
    if value == "turn on":
        print("Turning on: {}, {}".format(position[0], position[1]))
        value = "1"
    if value == "turn off":
        value = "0"
    if value == "toggle":
        if light_matrix[position[0]][position[1]] == "0":
            value = "1"
        else:
            value = "0"
    light_matrix[position[0]][position[1]] = value


def handle_operation(light_matrix, operation, start, end):
    start_x, start_y = [int(x) for x in start.split(',')]
    end_x, end_y = [int(x) for x in end.split(',')]
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            set_value(light_matrix, (x, y), operation)

def break_out_stuff(instruction):
    pattern = "([\w\s]+)\s(\d+\,\d+)\sthrough\s(\d+,\d+)"
    result = re.search(pattern, instruction)
    return (result[1], result[2], result[3])

def handle_instruction(light_matrix, line):
    operation, start, end = break_out_stuff(line)
    print("Operation: {}, start: {}, end: {}".format(operation, start, end))
    handle_operation(light_matrix, operation, start, end)

def main():
    light_matrix = build_initial_light_matrix()
    with open(INPUT_FILE) as input_file:
        for line in input_file:
            print("Raw line: {}".format(line))
            handle_instruction(light_matrix, line)
    print(light_matrix)
    print("There are {} lights turned on.".format(count_lights(light_matrix)))

if __name__ == "__main__":
    main()
