# module.py

def count_in_list(lst, item):
    """
    Count the occurrences of an item in a list.

    This function iterates through a list and counts how many times a
    specified item appears in the list.

    Parameters:
    lst (list): The list in which to count the occurrences of the item.
    item (any): The item to count in the list. This can be of any data
    type that supports equality comparison.

    Returns:
    int: The number of times the item appears in the list.
    """
    count = 0
    for i in lst:
        if i == item:
            count += 1
    return count
