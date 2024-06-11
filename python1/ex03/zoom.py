
import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt

# def convert_rgb_to_grayscale(image):
#     """
#     """
#     # Apply the formula ([0] + [1] + [2]) / 3 to each 1-D slice along axis 2
#     grayscale =  np.apply_along_axis(lambda x: np.mean(x), axis=2, arr=image).astype(np.uint8)

#     # Stack the grayscale values along the third axis to create a 3-channel grayscale image
#     return np.stack([grayscale], axis=-1)

def rgb_to_gray(rgb):
    gray = np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
    return np.stack([gray], axis=-1)


# def rgb_to_gray(img):
#     """"""
#     grayImage = np.zeros(img.shape)
#     R = np.array(img[:, :, 0])
#     G = np.array(img[:, :, 1])
#     B = np.array(img[:, :, 2])

#     R = (R *.299)
#     G = (G *.587)
#     B = (B *.114)

#     Avg = (R+G+B)
#     grayImage = img.copy()

#     for i in range(3):
#         grayImage[:,:,i] = Avg

#     return grayImage

def zoom(image):
    """
    """
    # new_image = convert_rgb_to_grayscale(image)
    new_image = rgb_to_gray(image)
    new_image = new_image[100:500, 440:840]
    
    shape_short = list(new_image.shape)
    shape_short.pop()
    print("New shape after slicing:", new_image.shape, " or ", tuple(shape_short))

    return new_image


def main():
    image = ft_load("animal.jpeg")
    print(image)
    new_image = zoom(image)
    print(new_image)
    plt.imshow(new_image, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
