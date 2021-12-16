def get_initial_state(filepath):
    lanternphish = {}
    with open(filepath, 'r') as infile:
        for line in infile:
            line = line.replace("\n", "")
            for x in line.split(','):
                x = int(x)
                lanternphish.setdefault(x, 0)
                lanternphish[x] += 1
    return lanternphish

def handle_day(phish):
    next_day = {}
    days_to_generate_new_phish = 7
    days_until_able_to_generate_new_phish = 2
    
    for phish_age, number_of_phish in phish.items():
        if phish_age == 0:
            one_phish = days_until_able_to_generate_new_phish+days_to_generate_new_phish-1
            two_phish = days_to_generate_new_phish-1
            next_day.setdefault(one_phish, 0)
            next_day[one_phish] += number_of_phish
            next_day.setdefault(two_phish, 0)
            next_day[two_phish] += number_of_phish
        else:
            phish_age-=1
            next_day.setdefault(phish_age, 0)
            next_day[phish_age] += number_of_phish
    return next_day

def main(filepath, num_days=1):
    phish = get_initial_state(filepath)
    print("Initial State:")
    print(phish)
    for day in range(num_days):
        print("------------------------------------------------------------------------------------")
        phish = handle_day(phish)
        print(phish)
        print("------------------------------------------------------------------------------------")
    print("Answer: {}".format(sum([y for x,y in phish.items()])))

if __name__ == "__main__":
    # main("./test_input.txt", 256)
    main("./input.txt", 256)
