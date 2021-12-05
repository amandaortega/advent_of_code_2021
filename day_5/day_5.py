import csv
import numpy as np

with open("day_5/input.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")

    all_lines = []

    for first_point, _separator, second_point in spamreader:
        x1, y1 = first_point.split(",")
        x2, y2 = second_point.split(",")
        all_lines.append([int(x1), int(y1), int(x2), int(y2)])

max_coord = int(max(max(all_lines)))
diagram_1 = np.zeros((max_coord + 1, max_coord + 1))
diagram_2 = np.zeros((max_coord + 1, max_coord + 1))

for x1, y1, x2, y2 in all_lines:
    if x1 == x2 or y1 == y2:
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)

        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                diagram_1[y, x] += 1
                diagram_2[y, x] += 1
    else:
        if x1 > x2 and y1 > y2:
            aux = x1
            x1 = x2
            x2 = aux
            aux = y1
            y1 = y2
            y2 = aux

        interval = range(abs(x1 - x2) + 1)

        if x2 > x1 and y2 > y1:
            for i in interval:
                diagram_2[y1 + i, x1 + i] += 1
        elif y1 > y2:
            for i in interval:
                diagram_2[y1 - i, x1 + i] += 1
        else:
            for i in interval:
                diagram_2[y1 + i, x1 - i] += 1

result1 = np.sum(diagram_1 > 1)
result2 = np.sum(diagram_2 > 1)
print(f"Part One: {result1}")
print(f"Part Two: {result2}")
