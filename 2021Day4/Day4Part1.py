class Board:
    def __init__(self):
        self.board_values = dict()
        self.board_all_numbers_sum = 0

    def add_entry(self, num, row_col_tuple):
        self.board_values[num] = row_col_tuple
        self.board_all_numbers_sum += num

    def get_number_location(self, num):
        if num in self.board_values:
            return self.board_values[num]
        else:
            return None


class BingoGame:
    def __init__(self):
        self.best_board = None
        self.best_board_moves_count = float('inf')
        self.number_order = list()
        self.best_board_selected_sum = None

    def set_number_order(self, input_file):
        numbers = next(input_file)
        numbers = numbers.rstrip().split(",")
        self.number_order = [int(num) for num in numbers]

    def build_board(self, input_file):
        board = Board()
        for row_index in range(5):
            column_index = 0
            line = next(input_file)
            row_array = line.rstrip().split()
            for number in row_array:
                number = int(number)
                board.add_entry(number, (row_index, column_index))
                column_index += 1
        return board

    def analyze_current_board(self, board):
        num_counter = 0
        selected_row_col = dict()
        selected_row_col['row'] = dict()
        selected_row_col['col'] = dict()
        selected_numbers_sum = 0
        for number in self.number_order:
            num_counter += 1
            if num_counter == self.best_board_moves_count:
                return
            location = board.get_number_location(number)
            if location:
                if location[0] in selected_row_col['row']:
                    selected_row_col['row'][location[0]].append(number)
                else:
                    selected_row_col['row'][location[0]] = [number]
                if location[1] in selected_row_col['col']:
                    selected_row_col['col'][location[1]].append(number)
                else:
                    selected_row_col['col'][location[1]] = [number]
                selected_numbers_sum += number
                if len(selected_row_col['row'][location[0]]) == 5:
                    self.best_board_moves_count = num_counter
                    self.best_board = board
                    self.best_board_selected_sum = selected_numbers_sum
                    return
                if len(selected_row_col['col'][location[1]]) == 5:
                    self.best_board_moves_count = num_counter
                    self.best_board = board
                    self.best_board_selected_sum = selected_numbers_sum
                    return

    def find_best_board(self, input_file):
        self.set_number_order(input_file)
        next_line = input_file.readline()
        while next_line:
            new_board = self.build_board(input_file)
            self.analyze_current_board(new_board)
            next_line = file.readline()

if __name__ == "__main__":
    input_file = "Day4Input.txt"
    file = open(input_file)
    bg = BingoGame()
    bg.find_best_board(file)
    print(bg.best_board.board_all_numbers_sum)
    print(bg.best_board_selected_sum)
    print(bg.best_board_moves_count)
    print(bg.number_order[bg.best_board_moves_count - 1])
    print(bg.best_board.board_all_numbers_sum -
          bg.best_board_selected_sum)
    file.close()
