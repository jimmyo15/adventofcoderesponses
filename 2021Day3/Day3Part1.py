class DiagnosticAnalyzer:
    def __init__(self):
        self.reversed_bit_array = []
        self.line_counter = 0

    def pad_array(self, line):
        line_diff = len(line) - len(self.reversed_bit_array)
        if line_diff > 0:
            for i in range(line_diff):
                self.reversed_bit_array.append(0)

    def process_bits(self, line):
        rbi = len(line) - 1
        li = 0
        while rbi >= 0:
            self.reversed_bit_array[rbi] += int(line[li])
            rbi -= 1
            li += 1

    def analyze_diagnostics(self, file_location):
        input_file = open(file_location)
        for line in input_file:
            self.pad_array(line.rstrip())
            self.process_bits(line.rstrip())
            self.line_counter += 1
        greeks = self.calculate_greeks()
        return greeks

    @staticmethod
    def convert_to_decimal(bit_array):
        value = 0
        for bit in bit_array:
            value = (value << 1) | bit
        return value

    def calculate_greeks(self):
        gamma_array = []
        epsilon_array = []
        mid_val = self.line_counter / 2
        i = len(self.reversed_bit_array) - 1
        while i >= 0:
            if self.reversed_bit_array[i] > mid_val:
                gamma_array.append(1)
                epsilon_array.append(0)
            else:
                gamma_array.append(0)
                epsilon_array.append(1)
            i -= 1
        gamma_val = DiagnosticAnalyzer().convert_to_decimal(gamma_array)
        epsilon_val = DiagnosticAnalyzer.convert_to_decimal(epsilon_array)
        return [gamma_val, epsilon_val]

if __name__ == "__main__":
    input_file = 'Day3Input.txt'
    da = DiagnosticAnalyzer()
    greeks = da.analyze_diagnostics(input_file)
    print(da.reversed_bit_array)
    print(da.line_counter/2)
    print(greeks[0])
    print(greeks[1])
    print(greeks[0] * greeks[1])