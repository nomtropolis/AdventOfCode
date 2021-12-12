def main(filepath):
    position = {"x": 0, "y": 0}
    with open(filepath, 'r') as inputfile:
        for directions in inputfile:
            direction, amount = directions.split(" ")
            position = handle_direction(position, direction, amount)
    print(position)
    print("{} x {} = {}".format(position["x"], position["y"], position["x"] * position["y"]))

def handle_direction(pos, _dir, amt):
    amt = int(amt)
    if _dir == "forward":
        pos["x"] = pos["x"] + amt
    elif _dir == "down":
        pos["y"] = pos["y"] + amt
    elif _dir == "up":
        pos["y"] = pos["y"] - amt
    return pos

if __name__ == "__main__":
    # main("./test_input.txt")
    main("./input.txt")
