import cv2


class MedianBlurProcessor:
    def __init__(self):
        pass

    def convert_to_blur(self, bgr_img):
        # TODO: Implement median blur
        if bgr_img is None:
            return None

        # Convert to Median Blur
        median_img = cv2.medianBlur(bgr_img, 5)
        return median_img
