import numpy as np
import matplotlib.pyplot as plt


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified file path and flip its RGB values along the third axis.

    Parameters:
    path (str): The file path of the image to load.

    Returns:
    np.ndarray: A NumPy array representing the loaded image with flipped RGB values along the third axis.
                The shape of the array is (height, width, channels), where channels represent the RGB values.
                If an error occurs during loading or processing the image, None is returned.

    Raises:
    This function does not raise any specific exceptions. Any exceptions that occur during image loading or processing
    are caught and printed to the console, and None is returned as the result.
    """
    try:
        image = plt.imread(path)
        print("The shape of image is:", image.shape)
        print(image)

        return image

    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    return None
