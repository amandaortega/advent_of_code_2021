import csv

horizontal_position = 0
depth_1 = 0
depth_2 = 0
aim = 0

with open("day_2/input.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    for row in spamreader:
        type_, value = row
        value = int(value)

        if type_ == "forward":
            horizontal_position += value
            depth_2 += aim * value
        elif type_ == "down":
            depth_1 += value
            aim += value
        elif type_ == "up":
            depth_1 -= value
            aim -= value

print(f"Part One: {horizontal_position * depth_1}")
print(f"Part One: {horizontal_position * depth_2}")
