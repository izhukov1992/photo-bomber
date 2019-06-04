import sys
import os

from PIL import Image
from PIL import ImageDraw

# Define default folders for searching and saving images, allowed extensions.
DEFAULT_INPUT_PATH = "."
DEFAULT_OUTPUT_PATH = "./output-images/"
IMAGES_EXTENSIONS = [".jpg", ".gif", ".png"]


def bomb_photos(input_path, output_path):
    """
    Lists image files, adds text and save new version.

    :param input_path: path for searching images.
    :param output_path: path for saving images with text.
    """
    try:
        for f in os.listdir(input_path):
            filename, ext = os.path.splitext(f)

            if ext.lower() not in IMAGES_EXTENSIONS:
                continue

            # Split name of file to get first name and last name of author,
            # capitalize and join name with space to combine full name for image.
            full_name = " ".join(name.capitalize()
                                 for name
                                 in filename.split("-"))

            img = Image.open(os.path.join(input_path, f))

            draw = ImageDraw.Draw(img)

            # Get dimensions of image and text caption.
            isize, tsize = img.size, draw.textsize(full_name)

            # Calculate vertical and horizontal position of caption
            # with 20 pixels of padding.
            position = tuple(map(lambda iside, tside: iside - tside - 20,
                                 isize, tsize))

            # Draw caption.
            draw.text(position, full_name, (255, 255, 255))

            # Create output directory, if it doesn't exist.
            if not os.path.isdir(output_path):
                os.mkdir(output_path)

            # Save new image to output directory.
            img.save(output_path + f)

    except BaseException as e:
        # Print error message, if input directory doesn't exist or
        # output directory doesn't exist or can't be created and exit.
        print(e)
        return


def main(args):
    """
    Main function extracts shell parameters and assigns default ones, if not passed.

    :param args: tuple of shell parameters excluding the first one.
    """
    input_path = DEFAULT_INPUT_PATH if args == [] else args.pop(0)
    output_path = DEFAULT_OUTPUT_PATH if args == [] else args.pop(0)
    bomb_photos(input_path, output_path)


if __name__ == '__main__':
    main(sys.argv[1:])
