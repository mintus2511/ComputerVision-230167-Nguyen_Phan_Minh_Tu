import cv2
import numpy as np


class DilationProcessor:
    def __init__(self):
        pass

    def apply_dilation_filter(self, bgr_img):
        # TODO: Implement dilation filter
        if bgr_img is None:
            return None

        # Convert to dilation filter
        kernel = np.ones((5, 5), np.uint8)
        dilation_img = cv2.dilate(bgr_img, kernel, iterations=1)
        return dilation_img
