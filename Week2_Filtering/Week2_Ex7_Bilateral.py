import cv2


class BilateralProcessor:
    def __init__(self):
        pass

    def apply_bilateral_filter(self, bgr_img):
        # TODO: Implement bilateral filter
        if bgr_img is None:
            return None

        # Convert to bilateral filter
        bilateral_img = cv2.bilateralFilter(
            bgr_img, d=9, sigmaColor=75, sigmaSpace=75)
        return bilateral_img
