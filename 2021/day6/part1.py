def get_initial_state(filepath):
    lanternphish = []
    with open(filepath, 'r') as infile:
        for line in infile:
            line = line.replace("\n", "")
            lanternphish.extend([int(x) for x in line.split(',')])
    return lanternphish

def handle_day(previous_day):
    today = []
    days_to_generate_new_phish = 7
    days_until_able_to_generate_new_phish = 2

    for phish in previous_day:
        if phish == 0:
            today.append(days_until_able_to_generate_new_phish+days_to_generate_new_phish-1)
            today.append(days_to_generate_new_phish-1)
        else:
            phish-=1
            today.append(phish)
    return today

def main(filepath, num_days=1):
    phish = get_initial_state(filepath)
    print("Initial State:")
    print(phish)
    for day in range(num_days):
        print("------------------------------------------------------------------------------------")
        phish = handle_day(phish)
        print(phish)
        print("------------------------------------------------------------------------------------")
    print("Answer: {}".format(len(phish)))

if __name__ == "__main__":
    main("./test_input.txt", 80)
    # main("./input.txt")
