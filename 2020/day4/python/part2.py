import re

# INPUT_FILE="../input.part2.valid.txt"
# INPUT_FILE="../input.part2.invalid.txt"
INPUT_FILE="../input.txt"
VALID_EYE_COLORS = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
VALID_HAIR_COLORS = re.compile('^#[0-9a-fA-F]{6}')


def valid_year_range(year, low, high):
    year = int(year)
    if year >= low and year <= high:
        return True
    return False


def valid_hair_color(thing):
    if VALID_HAIR_COLORS.match(thing):
        return True
    return False


class Passport(object):
    required_attributes = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    def __init__(self, init_string):
        self.__parse_init_string(init_string)

    def __parse_init_string(self, init_string):
        for x in init_string.split():
            k,v = x.split(":")
            setattr(self, k, v)

    def is_valid(self):
        for attr in self.required_attributes:
            try:
                thing = getattr(self, attr)
                if attr == "cid":
                    pass
                elif attr == "byr" and not valid_year_range(thing, 1920, 2002):
                    print("Failing validity check on birth year of: {}".format(thing))
                    return False
                elif attr == "iyr" and not valid_year_range(thing, 2010, 2020):
                    print("Failing validity check on issue year of: {}".format(thing))
                    return False
                elif attr == "eyr" and not valid_year_range(thing, 2020, 2030):
                    print("Failing validity check on exp year of: {}".format(thing))
                    return False
                elif attr == "hgt":
                    value, unit = (int(thing[:-2]), thing[-2:])
                    if unit == "cm" and value >= 150 and value <= 193:
                        pass
                    elif unit == "in" and value >= 59 and value <= 76:
                        pass
                    else:
                        print("Failing validity check on height of: {}".format(thing))
                        return False
                elif attr == "hcl" and not valid_hair_color(thing):
                    print("Failing validity check on hair color of: {}".format(thing))
                    return False
                elif attr == "ecl" and thing not in VALID_EYE_COLORS:
                    print("Failing validity check on eye color of: {}".format(thing))
                    return False
                elif attr == "pid":
                    try:
                        if len(str(thing)) == 9 and int(thing):
                            return True
                        print("Failing validity check on pid: {}".format(thing))
                        return False
                    except ValueError:
                        print("Failing validity check on pid of: {}".format(thing))
                        return False
            except AttributeError:
                print("Failing validity check on: {}  --  {}".format(attr, self))
                return False
        return True

def main():
    valid_passports = 0
    passports = []
    input_buffer = []
    with open(INPUT_FILE) as input_file:
        for line in input_file:
            if line == "\n":
                passport_string = " ".join(input_buffer)
                passport = Passport(passport_string)
                if passport.is_valid():
                    print("{} is valid".format(passport_string))
                    valid_passports += 1
                else:
                    print("{} is invalid".format(passport_string))
                input_buffer[:] = []
                print("--------------------------------------------------------------")
                continue
            input_buffer.append(line.replace("\n", ""))
    if input_buffer:
        passport = Passport(" ".join(input_buffer))
        if passport.is_valid():
            print("{} is valid".format(passport_string))
            valid_passports += 1
        else:
            print("{} is invalid".format(passport_string))
        print("--------------------------------------------------------------")            
    print("There are {} valid passports".format(valid_passports))


if __name__ == "__main__":
    main()
