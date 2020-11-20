INPUT_FILE = "../input.txt"

def get_smallest_side(x, y, z):
    return min([(x*y),(y*z),(x*z)])

def main():
    total_area = 0
    with open(INPUT_FILE) as input_file:
        for dimensions in input_file:
            x,y,z = [int(x) for x in dimensions.split('x')]
            area = (2*x*y) + (2*y*z) + (2*x*z)
            smallest_side = get_smallest_side(x, y, z)
            total_area += (area + smallest_side)
    print("Total Area: {}".format(total_area))

if __name__ == "__main__":
    main()
