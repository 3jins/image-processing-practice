import numpy as np
from PIL import Image
import os


def create_kernel(kernel_size, kernel_type):  # kernel a.k.a. mask
    # Exception handling
    if kernel_size % 2 == 0 or kernel_size < 0:
        print("Only odd numbers can be kernel size (current kernel size: {0}".format(kernel_size))
        exit(0)

    kernel = []
    divider = 1
    if kernel_type == 1:
        # mean kernel
        kernel = np.zeros([kernel_size, kernel_size]) + 1
    elif kernel_type == 2:
        # weighted mean kernel
        # TODO: Need to find the mask generating-rule and apply it.
        if kernel_size == 3:
            kernel = np.array([[1, 2, 1],
                               [2, 4, 2],
                               [1, 2, 1]])
        elif kernel_size == 5:
            kernel = np.array([[1, 4, 6, 4, 1],
                               [4, 16, 24, 16, 4],
                               [6, 24, 36, 24, 6],
                               [4, 16, 24, 16, 4],
                               [1, 4, 6, 4, 1]])
        else:
            print("Do not support the case kernel_size >= 7 because couldn\'t figure out the mask-generating rule.. :(")
            exit(0)
    else:
        # unsharp mask kernel
        # TODO: Should make a general mask-generating rule
        # Below are the known rules for making a Laplacian kernel.
        # 1. np.sum(laplacian_kernel) should be 0
        # 2. Values should be increased as they get closer
        # 3. Center value should be the smallest
        # 4. There is no strict rule to make a Laplacian kernel
        laplacian_kernel = []
        if kernel_size == 3:
            laplacian_kernel = np.array([[1, 1, 1],
                                         [1, -8, 1],
                                         [1, 1, 1]])
        elif kernel_size == 5:
            laplacian_kernel = np.array([[0, 0, 1, 0, 0],
                                         [0, 1, 2, 1, 0],
                                         [1, 2, -16, 2, 1],
                                         [0, 1, 2, 1, 0],
                                         [0, 0, 1, 0, 0]])
        else:
            print("Do not support the case kernel_size >= 7 because couldn\'t figure out the mask-generating rule.. :(")
            exit(0)
        kernel = - laplacian_kernel
        kernel[int(kernel_size / 2)][int(kernel_size / 2)] += 1
    return kernel


def apply_kernel(kernel, array, divider):
    return np.sum(np.multiply(kernel, array)) / divider


def get_smoothed_img(array, kernel, divider, kernel_size):
    if kernel_size % 2 == 0:
        return False

    # Exclude peripheral values from the calculation
    output_array = np.array(img, dtype=np.uint8)
    edge_start = int((kernel_size - 1) / 2)
    edge_y_end = img.shape[0] - edge_start
    edge_x_end = img.shape[1] - edge_start

    # Apply the mask
    for i in range(edge_start, edge_y_end):
        for j in range(edge_start, edge_x_end):
            output_px = apply_kernel(
                kernel,
                img[(i - edge_start):(i - edge_start + kernel_size), (j - edge_start):(j - edge_start + kernel_size)],
                divider)
            # Prevent an overflow
            if output_px > 255:
                output_px = 255
            if output_px < 0:
                output_px = 0
            output_array[i][j] = output_px
    return output_array


if __name__ == '__main__':
    file_name = './sample.jpg'
    save_file_name = ''

    # Get filtering method
    print("Select the filtering method")
    print("1. mean filter")
    print("2. weighted mean filter")
    print("3. unsharp mask filter")
    print("> ", end='')
    filtering_method = int(input())
    if type(filtering_method) is not int:
        print("Only integers are permitted as a filtering method value")
    if filtering_method > 3 or filtering_method < 1:
        print("Only 1, 2, and 3 are permitted as a filtering method value")

    # Get kernel size
    print("Put kernel size plz")
    print("> ", end='')
    kernel_size = int(input())
    if type(kernel_size) is not int:
        print("Only integers are permitted as a kernel size value")

    try:
        # Load an image
        read = Image.open(file_name)

        # Convert the image into an array
        img = np.array(read, dtype=np.int32)

        # Determine the result file name
        if filtering_method == 1:
            save_file_name = './mean.jpg'
        elif filtering_method == 2:
            save_file_name = './weighted_mean.jpg'
        else:
            save_file_name = './unsharp_mask.jpg'

        # Get a kernel and a divider
        print("Converting the image...")
        kernel = create_kernel(kernel_size, filtering_method)
        divider = np.sum(kernel)

        # Get smoothed image
        output_array = get_smoothed_img(img, kernel, divider, kernel_size)

        # Convert an output array to an image
        output = Image.fromarray(output_array)

        # Save
        output.save(save_file_name)
    except FileNotFoundError as err:
        print("\"" + file_name + "\" is not found. Check the name and directory of the file.")

    print("Complete! Check the current directory(" + os.getcwd() + ") :)")
