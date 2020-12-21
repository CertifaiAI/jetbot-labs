from PIL import Image
import numpy as np
from processing import ImageProcessing


def read_image(im_file, to_numpy=False):
    im = Image.open(im_file)

    # PIL does not show image channel only (width, height)
    print(im.size)

    if to_numpy is True:
        im = np.array(im)

    return im


if __name__ == '__main__':

    # Initialize Image processing class
    imagetr = ImageProcessing()

    # Read images
    im1 = read_image("1.jpg", to_numpy=True)
    im2 = read_image("2.jpg", to_numpy=True)
    im3 = read_image("3.jpg", to_numpy=True)
    im4 = read_image("4.jpg", to_numpy=True)

    # Resize Image
    im1 = imagetr.resize_image(im1, choose_one_dim=True)
    im2 = imagetr.resize_image(im2, choose_one_dim=True)
    im3 = imagetr.resize_image(im3, choose_one_dim=True)
    im4 = imagetr.resize_image(im4, choose_one_dim=True)

    # Concat Horizontally
    hconcat_im1 = imagetr.concat_horizontal(im1, im2)
    hconcat_im2 = imagetr.concat_horizontal(im3, im4)

    # Concat Vertically
    vconcat_im = imagetr.concat_vertical(hconcat_im1, hconcat_im2)

    # Convert from ndarray to PIL and save
    Image.fromarray(vconcat_im).save("result.jpg")
