def main(filepath):
    position = {"x": 0, "y": 0}
    aim = 0
    with open(filepath, 'r') as inputfile:
        for directions in inputfile:
            direction, amount = directions.split(" ")
            position, aim = handle_direction(position, direction, amount, aim)
    print(position)
    print("{} x {} = {}".format(position["x"], position["y"], position["x"] * position["y"]))

def handle_direction(pos, _dir, amt, aim):
    amt = int(amt)
    if _dir == "forward":
        pos["x"] = pos["x"] + amt
        pos["y"] = pos["y"] + (amt * aim)
    elif _dir == "down":
        aim = aim + amt
    elif _dir == "up":
        aim = aim - amt
    return pos, aim

if __name__ == "__main__":
    # main("./test_input.txt")
    main("./input.txt")
