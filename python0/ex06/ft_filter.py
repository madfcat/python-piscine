# def comprehend(func, x):
#     if func and func(x):
#         return x
#     elif not func and bool(x):
#         return x

# def ft_filter(func, iterable):
#     """
# filter(function or None, iterable) --> filter object

# Return an iterator yielding those items of iterable for which function(item)
# is true. If function is None, return the items that are true.
#     """

#     result = [comprehend(func, x) for x in iterable]

#     return result

def ft_filter(func, iterable):
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    result = []

    for x in iterable:
        if func and func(x):
            result.append(x)
        elif not func and bool(x):
            result.append(x)

    return result
