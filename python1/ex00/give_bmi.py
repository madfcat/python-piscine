def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for a list of height and weight
    values.

    The BMI is calculated using the formula:
        BMI = weight / (height^2)

    Parameters:
    height (list[int | float]): A list of heights in meters.
    weight (list[int | float]): A list of weights in kilograms.

    Returns:
    list[int | float]: A list of BMI values corresponding to the provided
    height and weight values.

    Note:
    - The function assumes that height values are in meters. If height values
    are in centimeters,
      they should be converted to meters before calling this function.
    - The function processes pairs of height and weight up to the length of
    the shorter list.
    """
    try:
        result = []

        for x in range(min(len(height), len(weight))):
            result.append(weight[x] / (height[x] ** 2))
        
        return result

    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to a list of BMI values.

    This function checks if each BMI value in the list exceeds the specified
    limit.

    Parameters:
    bmi (list[int | float]): A list of BMI values.
    limit (int): The threshold limit to compare against the BMI values.

    Returns:
    list[bool]: A list of boolean values where each element is True if the
    corresponding BMI value exceeds the limit, and False otherwise.
    """
    try:
        return [x > limit for x in bmi]

    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    return None

