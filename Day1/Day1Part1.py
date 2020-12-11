"""
Iterate through the file
Use a dictionary to store values that have been seen
For each entry, check if the diff between 2020 and the value
currently being evaluated against the dict.  If the diff exists
return the value and its difference.  Multiply them together and
return the result.
Assumptions: All items in input file are integers.
Time O(n)
Space O(n)
"""

class ExpenseReportCalculator:
    def __init__(self, target_value):
        self.reviewed_amounts = {}
        self.target_value = target_value

    def find_values_summing_to_target(self, file_location):
        input_file = open(file_location)
        for line in input_file:
            diff = self.target_value - int(line)
            if diff in self.reviewed_amounts:
                self.reviewed_amounts = {}
                input_file.close()
                return diff, int(line)
            self.reviewed_amounts[int(line)] = True
        input_file.close()
        return None

    @staticmethod
    def multiply_values(values_to_multiply):
        if not values_to_multiply:
            return None
        calculated_value = 1
        for value in values_to_multiply:
            calculated_value *= value
        return calculated_value

if __name__ == '__main__':
    erc = ExpenseReportCalculator(2020)
    file = "Day1Input.txt"
    expense_output = erc.multiply_values(erc.find_values_summing_to_target(file))
    print(expense_output)