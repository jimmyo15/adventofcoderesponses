class SubmarineMover:
    def __init__(self):
        self.position = [0, 0]
        self.aim = 0

    @staticmethod
    def parse_line(line):
        split_line = line.split(' ')
        direction = split_line[0]
        magnitude = int(split_line[1])
        return direction, magnitude

    def move_position(self, direction, magnitude):
        if direction == "up":
            self.aim -= magnitude
        if direction == "down":
            self.aim += magnitude
        if direction == "forward":
            self.position[0] += magnitude
            self.position[1] += (magnitude * self.aim)

    def pilot_sub(self, file_location):
        input_file = open(file_location)
        for line in input_file:
            direction, magnitude = SubmarineMover().parse_line(line)
            self.move_position(direction, magnitude)
        input_file.close()
        return self.position


if __name__ == "__main__":
    sm = SubmarineMover()
    input_file = 'Day2Input.txt'
    position = sm.pilot_sub(input_file)
    print(position)
    print(position[0] * position[1])