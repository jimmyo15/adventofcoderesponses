class DepthAnalyzer:
    def __init__(self):
        self.val1 = -1
        self.val2 = -1
        self.val3 = -1

    def count_depth_increase(self, file_location):
        counter = 0
        input_file = open(file_location)
        self.initialize_data_set(input_file)
        for next_val in input_file:
            next_val = int(next_val)
            prior_val = self.val1 + self.val2 + self.val3
            current_val = self.val2 + self.val3 + next_val
            if current_val > prior_val:
                counter += 1
            self.shift_values(next_val)
        input_file.close()
        return counter

    def initialize_data_set(self, input_file):
        self.val1 = int(next(input_file))
        self.val2 = int(next(input_file))
        self.val3 = int(next(input_file))

    def shift_values(self, next_val):
        self.val1 = self.val2
        self.val2 = self.val3
        self.val3 = next_val



if __name__ == "__main__":
    file = "Day1Input.txt"
    da = DepthAnalyzer()
    increase_count = da.count_depth_increase(file)
    print(increase_count)