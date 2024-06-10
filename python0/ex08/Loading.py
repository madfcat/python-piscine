def ft_tqdm(lst: range) -> None:
    """
    Generator function to emulate the behavior of the tqdm library for
    tracking the progress of iterations over a range.

    Args:
        lst (range): The range object to iterate over. It should specify
        the start, stop, and step values.

    Yields:
        int: The current value of the iteration from the range object.

    Notes:
        This function prints a progress bar to the console, indicating
        the percentage completion of the iteration over the range.
        It uses a Unicode block character (█) to represent completed progress
        and an emoji (🭬) to indicate the current position.
        The progress bar updates dynamically in the console without
        printing new lines.
    """

    total = int((lst.stop - lst.start) / lst.step)
    COLUMNS = 66

    for x in lst:
        percent = min((int(1 + 100 * x / total), 100))
        progress = int((COLUMNS * percent) / 100)
        print(
            f"{percent:3}%|"
            f"{'█' * (progress - 1)}🭬"
            f"{'░' * (COLUMNS - progress)}| "
            f"{min(x + lst.step, total)}/{total}",
            end="\r"
        )
        yield x
