import sys


def whatis():
    """
    Checks if integer is odd or even.

    Raises:
    AssertionError: If more than one argument is provided
    """
    if (len(sys.argv) > 2):
        raise AssertionError("more than one argument is provided")

    if (len(sys.argv) == 2):
        if not sys.argv[1].isdigit():
            raise AssertionError("argument is not an integer")

        if not (int(sys.argv[1]) % 2):
            print("I'm Even.")
        else:
            print("I'm Odd.")


def main():
    """
    Main function that calls whatis function and handles exceptions
    """
    sys.tracebacklimit = 0
    try:
        whatis()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
