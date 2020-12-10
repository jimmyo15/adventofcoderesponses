"""
Iterate through the file
Use a dictionary to store values that have been seen
For each entry, take the diff from target value and set a new target value
Then iterate through the keys in the dictionary
Check if the diff between new target value and the newly iterated value exists
If the diff exists, return the value and its difference and the starting value.  Multiply them together and
return the result.
Assumptions: All items in input file are integers.
This can be expanded upon to 'i' numbers, with time complexity being O(n^(i-1))
What happens if a number is half of the new target?  It would look for itself and find in the dictionary.
That works if a number shows up more than once, but if only once it would return an incorrect answer.
Need to store the number of times a number occurs. <- Haven't solved for this yet in the below.
"""


class ExpenseReportCalculator:
    def __init__(self):
        self.reviewed_amounts = {}

    def initiate_report(self, file_location, target_value, num_count=2):
        input_file = open(file_location)
        vals = self.find_values_summing_to_target(input_file, target_value, num_count)  # include self.num_count here
        return vals

    def find_values_summing_to_target(self, iterable, target_value, num_count):
        if num_count == 2:
            for value in iterable:
                diff = target_value - int(value)
                if diff in self.reviewed_amounts:
                    self.reviewed_amounts = {}
                    return [diff, int(value)]
                self.reviewed_amounts[int(value)] = True
            return []
        else:
            for value in iterable:
                new_target_value = target_value - int(value)
                vals = self.find_values_summing_to_target(self.reviewed_amounts, new_target_value, num_count - 1)
                if not vals:
                    self.reviewed_amounts[int(value)] = True
                else:
                    vals.append(int(value))
                    self.reviewed_amounts = {}
                    return vals
            return []

    @staticmethod
    def multiply_values(values_to_multiply):
        if not values_to_multiply:
            return None
        calculated_value = 1
        for value in values_to_multiply:
            calculated_value *= value
        return calculated_value

if __name__ == '__main__':
    erc = ExpenseReportCalculator()
    file = "Day1Input.txt"
    expense_output = erc.multiply_values(erc.initiate_report(file, 2020, 3))
    print(expense_output)