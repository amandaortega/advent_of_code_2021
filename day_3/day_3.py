import csv
import numpy as np
from scipy import stats

with open("day_3/input.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    input = [list(row[0]) for row in spamreader]

# Part One
report = np.array(input).astype(int)
most_frequent = "".join([str(bit) for bit in stats.mode(report)[0][0]])
least_frequent = "".join(["0" if bit == "1" else "1" for bit in most_frequent])
most_frequent_decimal = int(most_frequent, 2)
least_frequent_decimal = int(least_frequent, 2)

print(f"Part One: {most_frequent_decimal * least_frequent_decimal}")

# Part Two
numbers_oxygen_generator_rating = report
numbers_CO2_scrubber_rating = report

for column in range(report.shape[1]):
    if numbers_oxygen_generator_rating.shape[0] > 1:
        mode_oxygen_generator, count_oxygen_generator = stats.mode(
            numbers_oxygen_generator_rating[:, column]
        )

        if count_oxygen_generator[0] * 2 == numbers_oxygen_generator_rating.shape[0]:
            most_common_bit_oxygen_generator = 1
        else:
            most_common_bit_oxygen_generator = mode_oxygen_generator[0]

        numbers_oxygen_generator_rating = numbers_oxygen_generator_rating[
            numbers_oxygen_generator_rating[:, column]
            == most_common_bit_oxygen_generator
        ]

    if numbers_CO2_scrubber_rating.shape[0] > 1:
        mode_CO2_scrubber_rating, count_CO2_scrubber_rating = stats.mode(
            numbers_CO2_scrubber_rating[:, column]
        )

        if count_CO2_scrubber_rating[0] * 2 == numbers_CO2_scrubber_rating.shape[0]:
            least_common_bit_CO2_scrubber = 0
        else:
            least_common_bit_CO2_scrubber = 0 if mode_CO2_scrubber_rating[0] == 1 else 1

        numbers_CO2_scrubber_rating = numbers_CO2_scrubber_rating[
            numbers_CO2_scrubber_rating[:, column] == least_common_bit_CO2_scrubber
        ]

oxygen_generator_rating = "".join(
    [str(bit) for bit in numbers_oxygen_generator_rating.tolist()[0]]
)
CO2_scrubber_rating = "".join(
    [str(bit) for bit in numbers_CO2_scrubber_rating.tolist()[0]]
)
result = int(oxygen_generator_rating, 2) * int(CO2_scrubber_rating, 2)
print(f"Part Two: {result}")
