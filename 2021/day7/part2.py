def get_positions(filepath):
    with open(filepath, 'r') as infile:
        for line in infile:
            line = line.replace('\n', '')
            return [int(x) for x in line.split(',')]

def calculate_cost(positions, position):
    cost = 0
    for k,v in positions.items():
        cost += sum(range(abs(k-position)+1)) * v
    return cost
            

def main(filepath):
    positions = get_positions(filepath)
    print(positions)
    position_dict = {}
    
    for x in positions:
        position_dict.setdefault(x, 0)
        position_dict[x] += 1
    
    costs = {}
    for i in range(max(positions)):
        costs[i] = calculate_cost(position_dict, i)

    answer = min(costs.values())
    print("Answer: {}".format(answer))
    

if __name__ == "__main__":
    # main("./test_input.txt")
    main("./input.txt")
