INPUT_FILE = "../input.txt"


class Node(object):
    def __init__(self, color, parent, children):
        self.color = color
        self.parent = parent
        self.children = children


def isolate_color_from_words(words):
    color = " ".join(words[:2])
    del words[:3]
    return color


def get_contains_from_words(words):
    word_str = " ".join(words)
    if word_str == "contain no other bags":
        return []
    del words[0]
    bags = " ".join(words).replace(" bags", "").replace(" bag", "").split(", ")
    return bags


def build_node_index():
    node_index = {}
    with open(INPUT_FILE) as input_file:
        for line in input_file:
            words = line[:-2].split(" ")
            bag_color = isolate_color_from_words(words)
            parent = Node(bag_color, [], [])
            
            for other_bag in get_contains_from_words(words):
                num_bags = int(other_bag[0:other_bag.find(" ")])
                clean_bag = other_bag[other_bag.find(" ") + 1:]
                
                for x in range(0, num_bags):
                    rule_node = Node(clean_bag, parent, [])
                    parent.children.append(rule_node)
                    
            node_index[bag_color] = parent
    return node_index


def add_bags_to_bag(bag, node_index):
    if bag.children:
        for i, child_bag in enumerate(bag.children):
            bag.children[i] = add_bags_to_bag(node_index[child_bag.color], node_index)
    return bag


def recurse_count(tree):
    count = 0
    for node in tree.children:
        count += 1
        count += recurse_count(node)
    return count


if __name__ == "__main__":
    node_index = build_node_index()
    bag_tree = add_bags_to_bag(node_index["shiny gold"], node_index)
    num_bags = recurse_count(bag_tree)
    print("The answer is: {}".format(num_bags))
