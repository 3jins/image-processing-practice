import numpy as np
from PIL import Image


def modify_contrast(img_arr, alpha):
    # Exception handling
    if img_arr == []:
        print("This is an empty image.")
        exit(0)

    for i in range(len(img_arr)):
        for j in range(len(img_arr[0])):
            px_candidate = img_arr[i][j] + (img_arr[i][j] - 128) * alpha
            if px_candidate < 0:
                img_arr[i][j] = 0
            elif px_candidate > 255:
                img_arr[i][j] = 255
            else:
                img_arr[i][j] = px_candidate
    return Image.fromarray(img_arr)


if __name__ == '__main__':
    file_name = './low_contrast.jpg'

    try:
        # Load an image
        img = Image.open(file_name)

        # Convert the image into an array
        img_arr = np.array(img)

        # Get alpha from the user
        print("Put alpha plz: ")
        alpha = float(input())

        # Modify contrast of the original image array and get a new image
        new_img = modify_contrast(img_arr, alpha)

        # Show the converted image
        new_img.show()
    except FileNotFoundError as err:
        print("\"" + file_name + "\" is not found. Check the name and directory of the file.")