def callLimit(limit: int):
    """Return a decorator that limits the number of times a function can be
    called."""
    count = 0

    def callLimiter(function):
        """Return a function that limits the number of times a function
        can be"""
        def limit_function(*args: any, **kwds: any):
            """Return a function that limits the number of times a function
            can be called."""
            try:
                nonlocal count
                count += 1
                if count <= limit:
                    function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} call too many times")
            except AssertionError as e:
                print("Error: ", e)
        return limit_function

    return callLimiter
