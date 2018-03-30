import numpy as np
from PIL import Image


# Test function
def print_histogram(histogram):
    for val, num_val in enumerate(histogram):
        print("{0}: {1}".format(val, num_val))


def generate_histogram(arr, min_val=0, max_val=255):
    histogram = [0] * (max_val - min_val + 1)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            histogram[arr[i][j]] += 1

    return histogram


def histogram_equalize(img_arr, min_val=0, max_val=255):
    # Exception handling
    if img_arr == []:
        print("This is an empty image.")
        exit(0)

    histogram = generate_histogram(arr=img_arr, max_val=max_val, min_val=min_val)
    num_pixel = len(img_arr) * len(img_arr[0])
    normalized_sums = [0] * len(histogram)
    sum = 0
    for val, num_vals in enumerate(histogram):
        sum += histogram[val] / num_pixel * max_val
        normalized_sums[val] = np.round(sum)

    return normalized_sums


def decode_normalized_sums(original_img_arr, normalized_sums):
    decoded_arr = np.zeros(np.shape(original_img_arr), dtype=np.uint8)
    for i in range(len(decoded_arr)):
        for j in range(len(decoded_arr[0])):
            decoded_arr[i][j] = normalized_sums[original_img_arr[i][j]]
    return Image.fromarray(decoded_arr)


if __name__ == '__main__':
    min_val = 0
    max_val = 255
    file_name = './low_contrast.jpg'

    try:
        # Load an image
        img = Image.open(file_name)

        # Convert the image into an array
        img_arr = np.array(img)

        # Get normalized sums from the image array
        normalized_sums = histogram_equalize(img_arr=img_arr, max_val=max_val, min_val=min_val)

        # Get histogram-equalized image from the normalized sums
        new_img = decode_normalized_sums(img_arr, normalized_sums)

        # Show the converted image
        new_img.show()
    except FileNotFoundError as err:
        print("\"" + file_name + "\" is not found. Check the name and directory of the file.")