class ft_filter:
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """

    def __init__(self, function, iterable):
        self.function = function if function is not None else lambda x: x
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self.iterator)  # Get the next item from the iterator
            if self.function(item):     # Apply the filter function
                return item
