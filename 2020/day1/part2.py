INPUT_FILE = "input.txt"

def check_sum(num, lines):
    tracker_min = 0
    tracker_max = len(lines) - 1
    line_count = 0
    while True:
        top_num = lines[tracker_max]
        bottom_num = lines[tracker_min]
        combo = num + bottom_num + top_num
        if tracker_max < 0:
            return 0        
        if combo == 2020:
            return lines[tracker_min] * lines[tracker_max] * num
        elif combo < 2020:
            tracker_min += 1
            continue
        elif combo > 2020:
            tracker_max -= 1
            continue
        if tracker_min >= len(lines - 1)/2:
            return 0

        

def main():
    lines = []
    with open(INPUT_FILE, "r") as input_file:
        for line in input_file:
            if line:
                lines.append(int(line.strip('\n')))
    lines.sort()

    line_count = 0
    for line in lines:
        answer = check_sum(line, lines[line_count:])
        if answer > 0:
            return answer
        line_count += 1

if __name__ == "__main__":
    thing = main()
    print(thing)
