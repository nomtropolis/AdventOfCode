from pprint import pprint
def get_most_common_at_position(list_, position):
    print("---------------------------------------in get_most_common_at_position-----------------------------------------------")
    print("For Position: {}".format(position))
    # counter = {0: 0, 1: 0}
    counter = {
        0: {
            'items': [],
            'count': 0
        },
        1: {
            'items': [],
            'count': 0
        }
    }
    for line in list_:
        this_item = int(line[position])
        counter[this_item]['count'] += 1
        counter[this_item]['items'].append(line)
        print(counter)        
    if counter[0]['count'] > counter[1]['count']:
        print("---------------------------------------end get_most_common_at_position-----------------------------------------------")
        return 0, counter
    elif counter[1]['count'] > counter[0]['count']:
        print("---------------------------------------end get_most_common_at_position-----------------------------------------------")
        return 1, counter
    else:
        print("---------------------------------------end get_most_common_at_position-----------------------------------------------")
        return 1, counter

def generate_matrix(filepath):
    print("----------------------------------------------start generate_matrix-------------------------------------------------------")
    all_values = []
    with open(filepath, "r") as infile:
        for line in infile:
            line = line[:-1]
            if line.strip() == "\n":
                continue
            all_values.append(line)
    pprint(all_values)
    print("----------------------------------------------end generate_matrix-------------------------------------------------------")
    return all_values

def flip_bit(thing_to_flip):
    if thing_to_flip == 0:
        return 1
    else:
        return 0

def main(filepath):
    # oxygen generator rating most common value in the current bit position
    # co2 scrubber rating least common value in the current bit position
    # 0110 0101 1100

    all_lines = generate_matrix(filepath)
    position = 0
    most_common_lines = all_lines
    least_common_lines = all_lines
    oxygen_generator_rating = None
    co2_scrubber_rating = None
    print(all_lines)
    while (oxygen_generator_rating is None) and (co2_scrubber_rating is None):
        most_common_at_position, counts = get_most_common_at_position(most_common_lines, position)
        print("For position {}, {} is the most common, there are {} items left that match the most common".format(position, most_common_at_position, len(counts[most_common_at_position]['items'])))
        least_common_at_position = flip_bit(most_common_at_position)
        if counts[most_common_at_position]['count'] == 1:
            oxygen_generator_rating = counts[most_common_at_position]['items'][0]
        if counts[least_common_at_position]['count'] == 1:
            co2_scrubber_rating = counts[least_common_at_position]['items'][0]
        most_common_lines = counts[most_common_at_position]['items']
        position += 1
    print(oxygen_generator_rating)
    answer = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
    print("Answer is: {}".format(answer))

if __name__ == "__main__":
    file_to_load = "test_input.txt"
    # file_to_load = "input.txt"
    main(file_to_load)
