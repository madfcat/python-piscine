from ft_filter import ft_filter
import sys


# def ispunct(c): return bool("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~".find(c))

def is_wrong_char(c): return not c.isalpha() and not c == " "


def validate_s(str):
    for c in str:
        if is_wrong_char(c):
            return False
    return True


def validate_argv():
    """
Validates arguments passed to the program

Raises:
    AssertionError:
        if more than 2 arguments passed,
        first argument is not a valid string,
        second argument is not an integer number
    """
    if (len(sys.argv) != 3) or not validate_s(sys.argv[1]) or not sys.argv[2].isdigit():
        raise AssertionError("the arguments are bad")


def main():
    sys.last_traceback = 0

    try:
        validate_argv()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(0)

    n = int(sys.argv[2])
    s_list = sys.argv[1].split(' ')

    words_list = [x for x in s_list if len(x) > n]
    print(words_list)


if __name__ == "__main__":
    main()
