class ft_filter:
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """

    def __init__(self, function, iterable):
        self.filtered_items = (x for x in iterable if function(x)) if function is not None else (x for x in iterable if x)
        self.iterator = iter(self.filtered_items)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)
