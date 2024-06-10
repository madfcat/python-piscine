import sys


# https://stackoverflow.com/questions/21235855/how-to-read-user-input-until-eof
# https://stackoverflow.com/questions/58826614/how-to-capture-ctrld-when-you-have-already-typed-soemthing-in-raw-input-but-hav
def building():
    """
    Counts letters in a string.

    Raises:
    AssertionError: If more than one argument is provided
    """
    string = ""
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    char_dict = {
        "count": 0,
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "space": 0,
        "digit": 0
    }

    if (len(sys.argv) > 2):
        raise AssertionError("more than one argument is provided")

    if (len(sys.argv) != 1):
        string = sys.argv[1]
    else:
        print("What is the text to count?")
        for line in sys.stdin:
            string += line

    for c in string:
        char_dict["count"] += 1
        char_dict["upper"] += c.isupper()
        char_dict["lower"] += c.islower()
        char_dict["punctuation"] += c in punctuation
        char_dict["space"] += c.isspace()
        char_dict["digit"] += c.isdigit()

    print(f"The text contains {char_dict['count']} letters")
    print(f"{char_dict['upper']} upper letters")
    print(f"{char_dict['lower']} lower letters")
    print(f"{char_dict['punctuation']} punctuation marks")
    print(f"{char_dict['space']} spaces")
    print(f"{char_dict['digit']} digits")


def main():
    sys.tracebacklimit = 0
    try:
        building()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
