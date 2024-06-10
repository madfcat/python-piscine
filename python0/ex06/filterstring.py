from ft_filter import ft_filter
import sys


def validate_argv():
    if (len(sys.argv) > 2):
        raise AssertionError("more than one argument is provided")


def main():
	sys.last_traceback = 0

	try:
		validate_argv()
	except Exception as e:
        print(f"{type(e).__name__}: {e}")

    print(filter.__doc__)


if __name__ == "__main__":
    main()
