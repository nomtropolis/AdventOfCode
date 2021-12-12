import sys

def main(filepath):
    with open(filepath, 'r') as infile:
        answer = do_things(infile)
        print(answer)

def do_things(infile):
    previous = 0
    line_count = 0
    num_increases = 0
    lines = [line for line in infile]
    counter = 0
    for x in range(len(lines)-2):
        a = int(lines[x])
        b = int(lines[x+1])
        c = int(lines[x+2])
        total = int(a + b + c)
        if total > previous:
            counter += 1
        previous = total
    counter = counter - 1 # get rid of first comparison
    return counter

    
if __name__ == "__main__":
    main("./input.txt")
