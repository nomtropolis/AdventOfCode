import sys

def main(filepath):
    with open(filepath, 'r') as infile:
        answer = do_things(infile)
        print(answer)

def do_things(infile):
    previous = 0
    line_count = 0
    num_increases = 0
    for line in infile:
        thing = int(line)
        print("Previous: {} . Current: {}".format(previous, thing))
        if line_count == 0:
            line_count += 1
            previous = thing
            continue
        if thing > previous:
            num_increases += 1
        previous = thing            
    return num_increases

if __name__ == "__main__":
    main("./input.txt")
