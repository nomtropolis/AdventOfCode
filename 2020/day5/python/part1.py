from math import ceil
INPUT_FILE = "../input.txt"

def reverse_binary_search(sequence, low, high):
    for item in sequence:
        span = ceil((high - low) / 2)
        if item == "0":
            high = high - span
        elif item == "1":
            low = low + span
    if sequence[-1] == "0":
        return low
    return high

def get_row_number(row):
    sequence = row.replace("F", "0").replace("B", "1")
    return reverse_binary_search(sequence, 0, 127)

def get_col_number(col):
    sequence = col.replace("L", "0").replace("R", "1")
    return reverse_binary_search(sequence, 0, 7)

def get_user_id_from_binary_space_partition(line):
    row_number = get_row_number(line[:7])
    col_number = get_col_number(line[7:])
    print("{} {}".format(row_number, col_number))
    return (row_number * 8) + col_number


def main():
    user_ids = []
    with open(INPUT_FILE) as input_file:
        for line in input_file:
            user_ids.append(get_user_id_from_binary_space_partition(line))
    print("Max user id: {}".format(max(user_ids)))

if __name__ == "__main__":
    main()
