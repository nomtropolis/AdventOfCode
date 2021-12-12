def main(filepath):
    # 0110 0101 1100
    gamma_count = {}
    # epsilon_count = {} epsilon is opposite gamma
    count = 0
    with open(filepath, "r") as infile:
        line_count = 0
        for line in infile:
            digit_count = 0
            for digit in line:
                if digit == "\n":
                    continue
                digit = int(digit)
                gamma_count.setdefault(digit_count, {})
                gamma_count[digit_count].setdefault(digit, 0)
                gamma_count[digit_count][digit] += 1
                digit_count += 1
            line_count += 1
            
    final_gamma = ""
    final_epsilon = ""
    
    for digit_count, digit_count_dict in gamma_count.items():
        if digit_count_dict[0] > digit_count_dict[1]:
            final_gamma += "0"
            final_epsilon += "1"
        elif digit_count_dict[0] < digit_count_dict[1]:
            final_gamma += "1"
            final_epsilon += "0"
        else:
            print("Must be equal / what does instruction say for equal number of values?")

    print("final_gamma: {}".format(final_gamma))
    print("final_epsilon: {}".format(final_epsilon))
    print("Product: {}({}) * {}({}) = {}".format(final_gamma,int(final_gamma,2),final_epsilon,int(final_epsilon,2),(int(final_gamma,2)*int(final_epsilon,2))))
if __name__ == "__main__":
    file_to_load = "test_input.txt"
    # file_to_load = "input.txt"
    main(file_to_load)
