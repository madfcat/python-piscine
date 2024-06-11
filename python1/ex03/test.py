import matplotlib.pyplot as plt
import numpy as np

def show_image_with_axes(image_array):
    fig, ax = plt.subplots()
    ax.imshow(image_array)

    # Add labels and scale to the axes
    ax.set_xlabel('X Axis Label')
    ax.set_ylabel('Y Axis Label')
    ax.set_title('Image with Axes and Scale')
    ax.grid(True)  # Show grid

    # Set scale (optional)
    ax.set_xlim(0, image_array.shape[1])  # Set x-axis scale
    ax.set_ylim(image_array.shape[0], 0)  # Set y-axis scale

    plt.show()

if __name__ == "__main__":
    # Create a sample NumPy array (replace this with your actual image array)
    # Example: A 100x100 random RGB image
    image_array = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)

    # Show the image with axes and scale using Matplotlib
    show_image_with_axes(image_array)