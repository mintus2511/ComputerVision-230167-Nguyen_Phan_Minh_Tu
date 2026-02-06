import cv2


class ThresholdingProcessor:
    def __init__(self):
        pass

    def apply_thresholding_filter(self, bgr_img):
        # TODO: Implement thresholding filter
        if bgr_img is None:
            return None

        # Convert to thresholding filter
        _, binary_img = cv2.threshold(bgr_img, 128, 255, cv2.THRESH_BINARY)
        return binary_img
