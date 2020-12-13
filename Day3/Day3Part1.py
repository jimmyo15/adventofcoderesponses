"""
Iterate over each line in the file.
Add the horizontal movement to the current index.
If current index is greater than the length of the line, wrap around to the front of the line using modulus.
Can use modulus to begin with and not need the if > line length condition.
If it is a '#' then increment counter.
"""


class PathAnalyzer():
    def __init__(self):
        pass

    @staticmethod
    def count_trees(list_of_items):
        row_counter = 1
        horizontal_index = 0
        tree_count = 0
        for row in list_of_items:
            string_item = str(row)
            if string_item[len(string_item) - 1] == "\n":
                string_length = len(string_item) - 1  # Due to line end character
            else:
                string_length = len(string_item)
            if string_item[horizontal_index % string_length] == '#':
                tree_count += 1
            horizontal_index += 3
            row_counter += 1
        return tree_count


if __name__ == "__main__":
    pa = PathAnalyzer()
    file_name = 'Day3Input.txt'
    file = open(file_name)
    trees = pa.count_trees(file)
    file.close()
    print(trees)
