def count_letters(string: str) -> dict:
    result = {}
    for letter in string:
        if not letter.isalpha():
            continue
        if result.get(letter) is not None:
            result[letter] += 1
        else:
            result[letter] = 1

    return result


if __name__ == '__main__':
    SENTENCE = 'Row Row Row Your Boat'
    counted_letters = count_letters(SENTENCE)

    for letter, count in counted_letters.items():
        print(f'{letter} appears {count} time{"s" if count > 1 else ""}')
