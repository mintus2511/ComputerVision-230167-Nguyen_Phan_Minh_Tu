import cv2


class SobelProcessor:
    def __init__(self):
        pass

    def apply_sobel_filter(self, bgr_img):
        # TODO: Implement median blur
        if bgr_img is None:
            return None

        # Convert to Median Blur
        sobel_img = cv2.Sobel(bgr_img, cv2.CV_64F, 1, 0, ksize=3)
        sobel_img = cv2.convertScaleAbs(sobel_img)
        return sobel_img
