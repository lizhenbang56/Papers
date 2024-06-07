import base64
import glob
import os
from pathlib import Path


def remove_file_extension(file_path):
    """
    Remove the file extension from a given file path.

    :param file_path: The file path from which to remove the extension.
    :return: The file path without the extension.
    """
    return str(Path(file_path).with_suffix(''))


def img_to_base64(image_path):
    """
    Convert an image to a base64 encoded string.

    :param image_path: The file path to the image.
    :return: Base64 encoded string of the image.
    """
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            return encoded_string.decode("utf-8")
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    img_dir = '测试图像/'
    save_dir = 'base64/'
    imgs = os.listdir(img_dir)
    for img_name in imgs:
        img_path = os.path.join(img_dir, img_name)
        base64_string = img_to_base64(img_path)

        if base64_string:
            save_path = os.path.join(save_dir, remove_file_extension(img_name)+'.txt')
            with open(save_path, 'w') as f:
                f.write(base64_string)


if __name__ == "__main__":
    main()