import numpy as np
import cv2


def ft_load(path: str) -> np.ndarray:
    try:
        image = cv2.imread(path)
        flipped_image = np.flip(image, axis=2)

        print("The shape of image is:", flipped_image.shape)

        return flipped_image

    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    return None
