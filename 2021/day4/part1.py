def process_input(filepath):
    line_count = 0
    numbers_to_draw = []
    boards = []
    board_number = 0
    current_board = []
    with open(filepath, "r") as infile:
        for line in infile:
            line = line[:-1]
            if line_count == 0:
                numbers_to_draw = line.split(",")
                line_count += 1
                continue
            if line == "" and current_board:
                board_copy = current_board[:]
                boards.append({'board_number': board_number, 'rows': board_copy})
                board_number += 1
                del current_board
                current_board = []
                continue
            elif line == "":
                continue
            current_row = [{"number": x.strip(" "), "called": 0} for x in line.split(" ") if x]
            current_board.append(current_row)
    if current_board:
        boards.append({'board_number': board_number, 'rows': current_board})
    result = (numbers_to_draw, boards)
    return result

def mark_board(drawn_number, board):
    for row in board['rows']:
        for number_dict in row:
            if number_dict["number"] == drawn_number:
                number_dict["called"] = 1

def mark_boards(drawn_number, boards):
    for board in boards:
        mark_board(drawn_number, board)

def print_board(board):
    print("+" + "-"*58 + "+")    
    for row in board['rows']:
        row_length = len(row)
        line_count = 0
        for number_dict in row:
            if number_dict["called"]:
                square = "[{}]".format(number_dict["number"])
            else:
                square = "{}".format(number_dict["number"])
            print("|{}|".format(square.center(10)), end="")
            line_count += 1
            if line_count == row_length:
                print("")
    print("+" + "-"*58 + "+")                

def print_boards(called_numbers, boards):
    print("Called Numbers: {}".format(", ".join(called_numbers)))
    for board in boards:
        print_board(board)

def check_board(board):
    for x in range(len(board)):
        row_check = sum([
            board['rows'][x][0]['called'],
            board['rows'][x][1]['called'],
            board['rows'][x][2]['called'],
            board['rows'][x][3]['called'],
            board['rows'][x][4]['called']
        ])
        if row_check == 5:
            return True
        column_check = sum([
            board['rows'][0][x]['called'],
            board['rows'][1][x]['called'],
            board['rows'][2][x]['called'],
            board['rows'][3][x]['called'],
            board['rows'][4][x]['called']
        ])
        if column_check == 5:
            return True

def check_boards(boards):
    for board in boards:
        winner = check_board(board)
        if winner:
            return True, board
    return False, []

def sum_of_board(board):
    total = 0
    for row in board['rows']:
        total += sum([int(x['number']) for x in row if not x['called']])
    return total

def main(filepath):
    numbers_to_draw, boards = process_input(filepath)
    called_numbers = []
    for drawn_number in numbers_to_draw:
        mark_boards(drawn_number, boards)
        called_numbers.append(drawn_number)
        # print_boards(called_numbers, boards)
        winner, board = check_boards(boards)
        if winner:
            board_sum = sum_of_board(board)
            answer = int(drawn_number) * board_sum
            print("Have winner at drawn number: {}".format(drawn_number))
            print("Winning board: ")
            print_board(board)
            print("Sum of board: {}".format(board_sum))
            print("Solution: {} * {} = {}".format(drawn_number, board_sum, answer))
            break


if __name__ == "__main__":
    main("./test_input.txt")
    # main("./input.txt")

