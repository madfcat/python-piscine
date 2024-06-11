import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    inverted = 255 - array

    try:
        plt.imshow(inverted)
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    return inverted


def ft_red(array) -> np.ndarray:
    """
    Returns an image array with only red channel values preserved.
    """
    red = array.copy()
    red[:, :, 1:] = 0

    try:
        plt.imshow(red)
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    return red


def ft_green(array) -> np.ndarray:
    """
    Returns an image array with only green channel values preserved.
    """
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0

    try:
        plt.imshow(green)
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    return green


def ft_blue(array) -> np.ndarray:
    """
    Returns an image array with only blue channel values preserved.
    """
    blue = array.copy()
    blue[:, :, :2] = 0

    try:
        plt.imshow(blue)
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    return blue


def ft_grey(array) -> np.ndarray:
    """
    Convert an RGB image to grayscale.

    Parameters:
    array (np.ndarray): Input 3D array representing an RGB image.

    Returns:
    np.ndarray: A copy of the input array converted to grayscale.
    """
    # Compute the average of the RGB values along the third axis
    grey = np.mean(array, axis=2)
    # Stack the grayscale values along the third axis to create a 3-channel
    # grayscale image
    grey = np.stack([grey, grey, grey], axis=-1)
    # Normalize pixel values to the range [0, 1]
    grey = grey.astype(float) / 255

    try:
        plt.imshow(grey)
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    return grey
