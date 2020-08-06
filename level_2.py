from typing import Tuple


def get_min_max(numbers: set) -> Tuple[int, int]:
    """ Returns tuple with index 0 min, and index 1 max """
    return min(numbers), max(numbers)


if __name__ == '__main__':
    SET = {15, 11, 8, 15, 32, 20}
    minimum, maximum = get_min_max(SET)
    print(f'Minimum is {minimum} and maximum is {maximum}')
