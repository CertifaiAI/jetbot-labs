import cv2
import numpy as np


class ImageTransformation:
    def __init__(self):
        # The size of individual image
        self.desired_size = (200, 200)

    def resize_image(self, input_image, choose_one_dim=False):
        resized_image = cv2.resize(input_image, self.desired_size)
        print("\nOriginal Image: {}, Resized Image: {}".format(input_image.shape, resized_image.shape))

        im_shape = resized_image.shape

        # We only one to get one set of dimension for easier processing.
        if choose_one_dim is True and len(im_shape) != 2:
            dim_chosen = 1
            print("Choosing dimension {}. Total dimension: {}".format(dim_chosen, im_shape))
            resized_image = resized_image[:, :, dim_chosen]

        return resized_image


class ImageProcessing(ImageTransformation):
    def __init__(self):
        super(ImageProcessing, self).__init__()

        # For error checking. OpenCV can only process numpy array
        self.image_object_type = np.ndarray

    def concat_horizontal(self, image1, image2):

        self.check_image_instance(image1, image2)
        self.check_image_dim(image1)
        self.check_image_dim(image2)

        # Perform horizontal concatenation
        return cv2.hconcat([image1, image2])

    def concat_vertical(self, image1, image2):

        self.check_image_instance(image1, image2)
        self.check_image_dim(image1)
        self.check_image_dim(image2)

        # Perform vertical concatenation
        return cv2.vconcat([image1, image2])

    def check_image_instance(self, image1, image2):
        # Check the type of object. Make sure it is the desired type. If not, raise error.

        if not isinstance(image1, self.image_object_type):
            raise TypeError("Only ndarray objects allowed. Get Image1 {}".format(type(image1)))

        if not isinstance(image2, self.image_object_type):
            raise TypeError("Only ndarray objects allowed. Get Image2 {}".format(type(image2)))

    def check_image_dim(self, image):
        # Check the dimension of object. Make sure it is in correct format. If not, raise error.
        img_shape = image.shape
        if len(img_shape) != len(self.desired_size):
            raise Exception("Image have extra dimension of {}".format(img_shape[2]))