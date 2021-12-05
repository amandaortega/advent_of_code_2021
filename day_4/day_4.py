import csv
import numpy as np


def read_boards():
    with open("day_4/input.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
        numbers = next(spamreader)

        board = []
        all_boards = []
        all_masks = []
        boards_won = []

        for row in spamreader:
            if len(row) == 0:
                if len(board) > 0:
                    all_boards.append(np.array(board))
                    all_masks.append(np.zeros_like(board, dtype=np.bool8))
                    boards_won.append(False)

                board = []
            else:
                board.append([int(number) for number in row if number != ""])

    numbers = [int(number) for number in numbers[0].split(",")]

    return (numbers, all_boards, all_masks, boards_won)


def run_bingo(numbers, all_boards, all_masks, boards_won):
    result_first = -1

    for number in numbers:
        for board, masks, board_index in zip(
            all_boards, all_masks, range(len(boards_won))
        ):
            if not boards_won[board_index]:
                indexes = np.where(board == number)

                if len(indexes) == 2:
                    row, column = indexes
                    masks[row, column] = 1

                    sum_rows = np.sum(masks, axis=0)
                    sum_columns = np.sum(masks, axis=1)

                    # Bingo!
                    if any(sum_rows == masks.shape[0]) or any(
                        sum_columns == masks.shape[1]
                    ):
                        if not any(boards_won):
                            result_first = np.sum(board * np.invert(masks)) * number

                        boards_won[board_index] = True

                        if all(boards_won):
                            result_last = np.sum(board * np.invert(masks)) * number
                            return (result_first, result_last)


numbers, all_boards, all_masks, boards_won = read_boards()
result_first, result_last = run_bingo(numbers, all_boards, all_masks, boards_won)  # type: ignore
print(f"Part One: {result_first}")
print(f"Part Two: {result_last}")
