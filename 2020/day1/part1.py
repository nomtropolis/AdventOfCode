INPUT_FILE = "input.txt"

def main():
    lines = []
    with open(INPUT_FILE, "r") as input_file:
        for line in input_file:
            if line:
                lines.append(int(line.strip('\n')))
    lines.sort()

    tracker_min = 0
    tracker_max = len(lines) - 1

    while True:
        combo = lines[tracker_min] + lines[tracker_max]
        if combo == 2020:
            return lines[tracker_min] * lines[tracker_max]
        elif combo < 2020:
            tracker_min += 1
            continue
        elif combo > 2020:
            tracker_max -= 1
            continue

if __name__ == "__main__":
    thing = main()
    print(thing)
