import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def rgb_to_grey(rgb):
    """
    Converts rgb to not mapped grey
    """
    grey = np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
    return np.stack([grey], axis=-1)


def zoom(image):
    """
    Crops an image to vertically from 100px to 500px and horizontally from
    440 to 840px.
    Returns: 400x400 px image array
    """
    new_image = image[100:500, 440:840]

    return new_image


def main():
    try:
        image = ft_load("animal.jpeg")
        print(image)

        new_image = rgb_to_grey(image)
        new_image = zoom(new_image)

        shape_short = list(new_image.shape)
        shape_short.pop()
        print("New shape after slicing:",
              new_image.shape, " or ", tuple(shape_short))
        print(new_image)

        plt.imshow(new_image, cmap='gray')
        plt.show()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
