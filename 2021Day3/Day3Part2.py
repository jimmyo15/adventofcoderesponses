class DiagnosticAnalyzer:

    @staticmethod
    def analyze_life_support(file_location):
        input_file = open(file_location)
        oxygen = DiagnosticAnalyzer().calculate_oxygen(input_file)
        input_file.close()
        input_file = open(file_location)
        co2 = DiagnosticAnalyzer().calculate_co2(input_file)
        input_file.close()
        return [oxygen, co2]

    @staticmethod
    def calculate_oxygen(iterable, position_index=0):
        index = position_index
        next_iterable = DiagnosticAnalyzer().get_most_common_array(iterable, index)
        if len(next_iterable) == 1:
            return int(next_iterable[0], 2)
        index += 1
        return DiagnosticAnalyzer().calculate_oxygen(next_iterable, index)

    @staticmethod
    def calculate_co2(iterable, position_index=0):
        next_iterable = DiagnosticAnalyzer().get_least_common_array(iterable, position_index)
        if len(next_iterable) == 1:
            return int(next_iterable[0], 2)
        position_index += 1
        return DiagnosticAnalyzer().calculate_co2(next_iterable, position_index)

    @staticmethod
    def get_most_common_array(iterable, position_index):
        binary_dict = dict()
        binary_dict[0] = []
        binary_dict[1] = []
        for element in iterable:
            if element[position_index] == "0":
                binary_dict[0].append(element.rstrip())
            else:
                binary_dict[1].append(element.rstrip())
        if len(binary_dict[0]) > len(binary_dict[1]):
            return binary_dict[0]
        else:
            return binary_dict[1]

    @staticmethod
    def get_least_common_array(iterable, position_index):
        binary_dict = dict()
        binary_dict[0] = []
        binary_dict[1] = []
        for element in iterable:
            if element[position_index] == "0":
                binary_dict[0].append(element.rstrip())
            else:
                binary_dict[1].append(element.rstrip())
        if len(binary_dict[0]) > len(binary_dict[1]):
            return binary_dict[1]
        else:
            return binary_dict[0]


if __name__ == "__main__":
    input_file = 'Day3Input.txt'
    da = DiagnosticAnalyzer()
    life_support_array = da.analyze_life_support(input_file)
    print(life_support_array[0])
    print(life_support_array[1])
    print(life_support_array[0] * life_support_array[1])