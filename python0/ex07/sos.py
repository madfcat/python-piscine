import sys


is_wrong_char = (lambda c: not c.isalpha() and not c == " ")


def validate_s(str):
    """
    Validates string with a lambda function.

    Returns:
        False if one of the character is not alphabetical or space.
        Otherwise, True.
    """
    for c in str:
        if is_wrong_char(c):
            return False
    return True


def validate_argv():
    """
    Validates arguments passed to the program

    Raises:
        AssertionError:
            if more than 1 arguments passed,
            argument is not a valid format string
    """
    if (len(sys.argv) != 2) or not validate_s(sys.argv[1]):
        raise AssertionError("the arguments are bad")


def convert_str_to_morse(str):
    """
    Converts string to morse code. String should be valid.

    Returns:
        string with morse code.
    """
    result = []
    NESTED_MORSE = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
        "3": "...--", "4": "....-", "5": ".....", "6": "-....",
        "7": "--...", "8": "---..", "9": "----.", " ": "/"
    }

    for c in str:
        result.append(NESTED_MORSE[c.upper()])
    return ' '.join(result)


def main():
    sys.last_traceback = 0

    try:
        validate_argv()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(0)

    print(convert_str_to_morse(sys.argv[1]))


if __name__ == "__main__":
    main()
