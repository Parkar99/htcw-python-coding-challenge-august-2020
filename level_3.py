def count_letters(string: str) -> dict:
    result = {}
    for letter in string:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1

    return result


if __name__ == '__main__':
    SENTENCE = 'Row Row Row Your Boat'
    counted_letters = count_letters(SENTENCE)

    for l, c in counted_letters.items():
        print(f'{l} appears {c} time{"s" if c > 1 else ""}')
