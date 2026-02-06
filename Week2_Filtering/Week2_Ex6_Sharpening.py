import cv2
import numpy as np


class SharpeningProcessor:
    def __init__(self):
        pass

    def apply_sharpening_filter(self, bgr_img):
        # TODO: Implement median blur
        if bgr_img is None:
            return None

        kernel = np.array([[0, 1, 0],
                           [1, 5, 1],
                           [0, 1, 0]])
        # Convert to Median Blur
        sharpening_img = cv2.filter2D(bgr_img, -1, kernel)
        return sharpening_img
