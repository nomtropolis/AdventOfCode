import statistics

def get_positions(filepath):
    with open(filepath, 'r') as infile:
        for line in infile:
            line = line.replace('\n', '')
            return [int(x) for x in line.split(',')]
            

def main(filepath):
    positions = get_positions(filepath)
    print(positions)
    median = statistics.median(positions)
    fuel_used = 0
    for crab_tank in positions:
        fuel_used += abs(crab_tank - median)
    print("Answer: {}".format(fuel_used))
    

if __name__ == "__main__":
    # main("./test_input.txt")
    main("./input.txt")
