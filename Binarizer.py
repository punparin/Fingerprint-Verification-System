import cv2
import numpy as np

#-----------------------------
class Binarizer:
    def binarize(self, fpImg):
        retval, binImg = cv2.threshold(fpImg, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        return binImg

#-----------------------------
if __name__ == "__main__":
    img = cv2.imread("FP DB (subset)/1_1.bmp", cv2.IMREAD_GRAYSCALE)
    binImg = Binarizer().binarize(img)
    cv2.imshow("binary", binImg)
    cv2.imwrite('test.bmp',binImg)
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------
