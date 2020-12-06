INPUT_FILE="../input.txt"
REQUIRED_ATTRIBUTES = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


class Passport(object):

    def __init__(self, init_string):
        self.__parse_init_string(init_string)

    def __parse_init_string(self, init_string):
        print("Init string: {}".format(init_string))
        for x in init_string.split():
            print("Init phrase: {}".format(x))
            k,v = x.split(":")
            setattr(self, k, v)

    def is_valid(self):
        for attr in REQUIRED_ATTRIBUTES:
            try:
                thing = getattr(self, attr)
            except AttributeError:
                print("Failing validity check on: {}  --  {}".format(attr, self))
                return False
        return True


def handle_complete_line(input_buffer, valid_passports):
    passport = Passport(" ".join(input_buffer))
    if passport.is_valid():
        return 1
    return 0


def main():
    valid_passports = 0
    input_buffer = []
    with open(INPUT_FILE) as input_file:
        for line in input_file:
            if line == "\n":
                valid_passports += handle_complete_line(input_buffer, valid_passports)
                input_buffer[:] = []
                continue
            input_buffer.append(line)
    if input_buffer:
        valid_passports += handle_complete_line(input_buffer, valid_passports)
    print("There are {} valid passports".format(valid_passports))


if __name__ == "__main__":
    main()
 
