from pprint import pprint

#INPUT_FILE = "../input.example.txt"
DEBUG = True
INPUT_FILE = "../input.txt"

def debug_decorator(func):
    def wrapper(*args, **kwargs):
        if DEBUG:
            print("Calling: {} with positional arg {} and keyword args {}".format(func.__name__, args, kwargs))
        result = func(*args, **kwargs)
        if DEBUG:
            print("Result: {}".format(result))
            print("Completed calling: {}\n".format(func.__name__))
        return result
    return wrapper

@debug_decorator
def isolate_color_from_words(words):
    color = " ".join(words[:2])
    del words[:3]
    return color

@debug_decorator
def get_contains_from_words(words):
    word_str = " ".join(words)
    if word_str == "contain no other bags":
        return []
    del words[0]
    bags = " ".join(words).replace(" bags", "").replace(" bag", "").split(", ")
    return bags

@debug_decorator
def build_inverse_rule_dictionary():
    can_be_contained_by = {}
    with open(INPUT_FILE) as input_file:
        for line in input_file:
            line = line[:-2]
            words = line.split(" ")
            bag_color = isolate_color_from_words(words)
            can_contain = get_contains_from_words(words)
            for other_bag in can_contain:
                clean_bag = other_bag[other_bag.find(" ") + 1:]
                can_be_contained_by.setdefault(clean_bag, []).append(bag_color)
    return can_be_contained_by

@debug_decorator
def recurse_count(base, all_colors, counted_colors=[]):
    count = 0
    for color in base:
        print("Working on: {}".format(color))
        if color not in counted_colors:
            count += 1
            counted_colors.append(color)
        if all_colors.get(color, []):
            count += recurse_count(all_colors[color], all_colors, counted_colors)
    return count

def main(rule_dictionary):
    shiny_gold_bag_holders = recurse_count(rule_dictionary["shiny gold"], rule_dictionary)
    print("Answer is: {}".format(shiny_gold_bag_holders))

if __name__ == "__main__":
    rules_dictionary = build_inverse_rule_dictionary()
    main(rules_dictionary)
