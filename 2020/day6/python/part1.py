INPUT_FILE = "../input.txt"
# INPUT_FILE = "../input.example.txt"


def main():
    group_buffer = []
    final_answer = 0
    with open(INPUT_FILE) as input_file:
        for line in input_file:
            if line == "\n":
                group_answer = len(set(group_buffer))
                print("Adding {} to final_answer".format(group_answer))
                final_answer += group_answer
                group_buffer[:] = []
                continue
            for char in line:
                if char != "\n":
                    group_buffer.append(char)
    if group_buffer:
        final_answer += len(set(group_buffer))
    print("The answer is {}".format(final_answer))

if __name__ == "__main__":
    main()
