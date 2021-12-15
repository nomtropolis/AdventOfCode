import pdb

class line(object):
    def __init__(self, raw_line):
        raw_line = raw_line[:-1]
        comma_coords = raw_line.split(' -> ')
        start_x,start_y = comma_coords[0].split(',')
        stop_x,stop_y = comma_coords[1].split(',')
        self.max_x = 0
        self.max_y = 0
        self.line_type = "UNKNOWN"
        self.is_diagonal = self.__check_diagonal(start_x, start_y, stop_x, stop_y)
        self.coords = []
        self.coords = self.__get_coords(start_x, start_y, stop_x, stop_y)
        self.current_position = 0

    def __repr__(self):
        return "{}: [ {} ]".format(self.line_type, " ".join(["{},{}".format(x[0],x[1]) for x in self.coords]))

    def __str__(self):
        return "{}: [ {} ]".format(self.line_type, " ".join(["{},{}".format(x[0],x[1]) for x in self.coords]))

    def __check_diagonal(self, start_x, start_y, stop_x, stop_y):
        if (start_x != stop_x) and (start_y != stop_y):
            return True
        return False

    def __get_coords(self, start_x, start_y, stop_x, stop_y):
        # print("{} line: {},{} -> {},{}".format(self.line_type, start_x, start_y, stop_x, stop_y))
        x_coords = self.__get_coords_for_axis(start_x, stop_x)
        # print(x_coords)
        y_coords = self.__get_coords_for_axis(start_y, stop_y)
        if (len(x_coords) > len(y_coords)) and (len(y_coords) == 1):
            self.line_type = "HORIZONTAL"
            self.max_y = y_coords[0]
            while len(y_coords) < len(x_coords):
                y_coords.append(y_coords[0])
        elif (len(y_coords) > len(x_coords)) and (len(x_coords) == 1):
            self.line_type = "VERTICAL"
            self.max_x = x_coords[0]
            while len(x_coords) < len(y_coords):
                x_coords.append(x_coords[0])
        else:
            self.line_type = "DIAGONAL"
        return list(zip(x_coords, y_coords))

    def __get_coords_for_axis(self, start, stop):
        # print("Getting coords for axis: start: {}, stop: {}".format(start, stop))
        flip = False
        if int(start) < int(stop):
            low = int(start)
            high = int(stop)
        else:
            flip = True
            low = int(stop)
            high = int(start)
        result = [int(x) for x in range(low, high+1)]
        if flip:
            # print("Flipping")
            result = result[::-1]
        return result

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_position == len(self.coords):
            raise StopIteration
        item = self.coords[self.current_position]
        self.current_position = self.current_position + 1
        return item

def get_lines(filepath, use_diagonals=False):
    lines = []
    with open(filepath, 'r') as infile:
        for raw_line in infile:
            this_line = line(raw_line)
            # print(this_line)
            if this_line.is_diagonal and not use_diagonals:
                continue
            lines.append(this_line)
    return lines

def make_grid(grid_size):
    return [[0] * grid_size for _ in range(grid_size)]

def print_grid(grid):
    for row in grid:
        print(row)


def main(filepath, grid_size):
    lines = get_lines(filepath, True)
    grid = make_grid(grid_size)
    answer = 0
    for this_line in lines:
        print("Working on line: {}".format(this_line))
        for coord in iter(this_line):
            grid[coord[1]][coord[0]] = grid[coord[1]][coord[0]] + 1
            if grid[coord[1]][coord[0]] == 2:
                answer += 1
    print("-----------------------------------------------------------------")
    print_grid(grid)
    print("-----------------------------------------------------------------")
    print("Answer: {}".format(answer))
    

if __name__ == "__main__":
    main("./test_input.txt", grid_size=10)
    # main("./input.txt", grid_size=1000)
