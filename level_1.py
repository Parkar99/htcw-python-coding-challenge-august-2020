def count_duplicate_numbers(numbers: tuple, to_find: int) -> int:
    return numbers.count(to_find)


if __name__ == '__main__':
    NUMBERS = (1, 1, 2, 3, 4, 1, 5, 6, 7, 1)
    NUMBER_TO_FIND = 1
    duplicate_ones = count_duplicate_numbers(NUMBERS, NUMBER_TO_FIND)

    print(f'Number of duplicate {NUMBER_TO_FIND}\'s in the tuple is {duplicate_ones}')
