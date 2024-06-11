import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    inverted = 255 - array
    return inverted


def ft_red(array) -> np.ndarray:
    """
    Returns an image array with only red channel values preserved.
    """
    red = array.copy()
    red[:, :, 1:] = 0
    
    return red


def ft_green(array) -> np.ndarray:
    """
    Returns an image array with only green channel values preserved.
    """
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    
    return green


def ft_blue(array) -> np.ndarray:
    """
    Returns an image array with only blue channel values preserved.
    """
    blue = array.copy()
    blue[:, :, :2] = 0
    
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
    # Stack the grayscale values along the third axis to create a 3-channel grayscale image
    grey = np.stack([grey, grey, grey], axis=-1)
    # Normalize pixel values to the range [0, 1]
    grey = grey.astype(float) / 255
    
    return grey


def main():
    try:
        image = ft_load("landscape.jpg")
        inverted = ft_invert(image)
        red = ft_red(image)
        green = ft_green(image)
        blue = ft_blue(image)
        grey = ft_grey(image)
        
        plt.imshow(image)
        plt.show()
        
        plt.imshow(inverted)
        plt.show()

        plt.imshow(red)
        plt.show()

        plt.imshow(green)
        plt.show()

        plt.imshow(blue)
        plt.show()

        plt.imshow(grey)
        plt.show()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")

if __name__ == "__main__":
    main()