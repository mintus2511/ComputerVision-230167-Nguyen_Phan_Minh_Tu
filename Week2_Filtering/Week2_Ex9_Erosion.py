import cv2
import numpy as np


class ErosionProcessor:
    def __init__(self):
        pass

    def apply_erosion_filter(self, bgr_img):
        # TODO: Implement erosion filter
        if bgr_img is None:
            return None

        # Convert to erosion filter
        kernel = np.ones((5, 5), np.uint8)
        erosion_img = cv2.erode(bgr_img, kernel, iterations=1)
        return erosion_img
