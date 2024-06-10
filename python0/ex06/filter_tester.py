from ft_filter import ft_filter


def more_than_five(x):
    if x > 5:
        return True
    else:
        return False


def print_arr(arr):
    for x in arr:
        print(x)


def main():
    print(filter.__doc__)

    print(ft_filter.__doc__)

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bigger_numbers = filter(None, numbers)
    print("filter:")
    print_arr(bigger_numbers)
    print("\n")

    bigger_numbers2 = ft_filter(None, numbers)
    print("ft_filter:")
    print_arr(bigger_numbers2)
    print("\n")

    print("filter:")
    bigger_numbers3 = filter(more_than_five, numbers)
    print_arr(bigger_numbers3)
    print("\n")

    bigger_numbers4 = ft_filter(more_than_five, numbers)
    print("ft_filter:")
    print_arr(bigger_numbers4)
    print("\n")


if __name__ == "__main__":
    main()
