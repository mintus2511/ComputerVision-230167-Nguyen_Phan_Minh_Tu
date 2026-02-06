import cv2


class laplacianProcessor:
    def __init__(self):
        pass

    def apply_laplacian_filter(self, bgr_img):
        # TODO: Implement median blur
        if bgr_img is None:
            return None

        # Convert to Median Blur
        laplacian_img = cv2.Laplacian(bgr_img, cv2.CV_64F)
        laplacian_img = cv2.convertScaleAbs(laplacian_img)
        return laplacian_img
