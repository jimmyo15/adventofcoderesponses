class DepthAnalyzer:
    @staticmethod
    def depth_increase_count(file_location):
        counter = 0
        input_file = open(file_location)
        prior_val = int(next(input_file))
        for current_val in input_file:
            current_val = int(current_val)
            if current_val > prior_val:
                counter += 1
            prior_val = current_val
        input_file.close()
        return counter

if __name__ == "__main__":
    file = "Day1Input.txt"
    increase_count = DepthAnalyzer().depth_increase_count(file)
    print(increase_count)