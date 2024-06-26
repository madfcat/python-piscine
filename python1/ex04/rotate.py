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


def transpose(matrix):
    """
    Transposes a matrix
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new empty matrix to store the transposed values
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Swap elements to transpose the matrix
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return np.array(transposed_matrix)


def main():
    """
    Main function that loads an image, converts it to greyscale, crops it,
    transposes it, reshapes it to 2D, and displays the image.
    """
    try:
        image = ft_load("animal.jpeg")

        new_image = rgb_to_grey(image)
        new_image = zoom(new_image)

        shape_short = list(new_image.shape)
        shape_short.pop()
        print("The shape of image is:", new_image.shape,
              " or ", tuple(shape_short))
        print(new_image)

        new_image = transpose(new_image)
        new_image_2d = new_image.reshape(
            new_image.shape[0], new_image.shape[1])
        print("New shape after Transpose:", new_image_2d.shape)
        print(new_image_2d)

        plt.imshow(new_image, cmap='gray')
        plt.show()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
