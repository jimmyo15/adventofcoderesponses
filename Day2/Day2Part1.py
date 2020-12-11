"""
A couple of options that come to mind, but the most direct one also seems like it would be the fastest.
For each row, parse the item and set the target letter, min, and max value.  Go through the password character
by character and keep a counter of the letter in question.  If the counter is >= min AND <= max, then return True (1).
"""
import re


class PasswordAnalyzer():
    def __init__(self):
        pass

    @staticmethod
    def record_parser(record):
        record_attributes = {}
        regex = '^(\d+)-(\d+) ([a-zA-Z]): ([a-zA-z]+)$'
        parsed_record = re.match(regex, record)
        record_attributes["min"] = int(parsed_record.groups()[0])
        record_attributes["max"] = int(parsed_record.groups()[1])
        record_attributes["target_letter"] = parsed_record.groups()[2]
        record_attributes["password"] = parsed_record.groups()[3]
        return record_attributes

    @staticmethod
    def password_analyzer(iterable):
        correct_password_counter = 0
        for item in iterable:
            target_letter_counter = 0
            parsed_item = PasswordAnalyzer.record_parser(item)
            for character in parsed_item["password"]:
                if character == parsed_item["target_letter"]:
                    target_letter_counter += 1
            if parsed_item["min"] <= target_letter_counter <= parsed_item["max"]:
                correct_password_counter += 1
        return correct_password_counter


if __name__ == "__main__":
    file = 'Day2Input.txt'
    input_file = open(file)
    pa = PasswordAnalyzer()
    count = pa.password_analyzer(input_file)
    input_file.close()
    print(count)
