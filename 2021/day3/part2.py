from pprint import pprint
import operator

def clean_input(filepath):
    all_values = []
    with open(filepath, "r") as infile:
        for line in infile:
            line = line[:-1]
            if line.strip() == "\n":
                continue
            all_values.append(line)
    
    return all_values

def get_values(matrix, position, operand, default):
    counter = {
        0: {'items': [], 'count': 0},
        1: {'items': [], 'count': 0}
    }
    for line in matrix:
        this_item = int(line[position])
        counter[this_item]['count'] += 1
        counter[this_item]['items'].append(line)
    if operand(counter[0]['count'], counter[1]['count']):
        return counter[0]['items']
    elif operand(counter[1]['count'], counter[0]['count']):
        return counter[1]['items']
    else:
        return counter[default]['items']

def main(filepath):
    # oxygen generator rating most common value in the current bit position
    # co2 scrubber rating least common value in the current bit position
    all_lines = clean_input(filepath)
    position = 0
    oxygen_generator_rating = None
    co2_scrubber_rating = None
    most_common,least_common = (all_lines, all_lines)
    while not oxygen_generator_rating or not co2_scrubber_rating:
        if len(most_common) == 1:
            oxygen_generator_rating = most_common[0]
            print("Found oxygen generator rating: {}".format(oxygen_generator_rating))
        else:
            most_common = get_values(most_common, position, operator.gt, 1)

        if len(least_common) == 1:
            co2_scrubber_rating = least_common[0]
            print("Found co2 scrubber rating: {}".format(co2_scrubber_rating))
        else:
            least_common = get_values(least_common, position, operator.lt, 0)
        position += 1
    print("Answer is: {} * {} = {}".format(
        int(oxygen_generator_rating, 2),
        int(co2_scrubber_rating, 2),
        int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)        
    ))

if __name__ == "__main__":
    # file_to_load = "test_input.txt"
    file_to_load = "input.txt"
    main(file_to_load)
