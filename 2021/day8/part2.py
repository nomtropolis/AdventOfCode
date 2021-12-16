def get_notations(filepath):
    notations = []
    with open(filepath, 'r') as infile:
        for line in infile:
            line = line.replace('\n', '')
            notations.append(line)
    return notations

def convert_to_number(segment):
    # 0 : 6
    # 1 : 2
    # 2 : 5
    # 3 : 5
    # 4 : 4
    # 5 : 5
    # 6 : 6
    # 7 : 3
    # 8 : 7
    # 9 : 6
    seg_length = len(segment)
    if seg_length == 2:
        return 1
    elif seg_length == 4:
        return 4
    elif seg_length == 3:
        return 7
    elif seg_length == 7:
        return 8
    else:
        return None

def main(filepath):
    notations = get_notations(filepath)
    answer = 0
    for notation in notations:
        pattern, output = notation.split(' | ')
        for x in output.split(' '):
            number = convert_to_number(x)
            if number is not None:
                answer += 1
    print(answer)

if __name__ == "__main__":
    # main("./test_input.txt")
    main("./input.txt")
