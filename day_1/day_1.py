from typing import Counter
from numpy import genfromtxt

input = list(genfromtxt("day_1/input.csv"))

# Part One
counting = 0
for index in range(1, len(input)):
    if input[index] > input[index - 1]:
        counting += 1

print(f"Part One: {counting}")

# Part Two
counting = 0
for index in range(3, len(input)):
    if sum(input[index - 2 : index + 1]) > sum(input[index - 3 : index]):
        counting += 1

print(f"Part Two: {counting}")
