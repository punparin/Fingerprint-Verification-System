import cv2
import numpy as np
from Binarizer import Binarizer
import FpSegmentator
from OfDetector import OfDetector
from GaborFilterbank import GaborFilterbank
from FpSegmentator import FpSegmentator

#-----------------------------
class FpEnhancer:
    def createMask(self, segmentedImg, n = 16):
        rows, cols = segmentedImg.shape
        mask = np.zeros(segmentedImg.shape, dtype = np.uint8)
        white = np.ones((n, n), dtype = np.uint8)
        white*=255
        for i in range(0, rows, n):
            for j in range(0, cols, n):
                block = segmentedImg[i:i+n, j:j+n]
                temp = white==block
                if temp.all():
                    mask[i:i+n, j:j+n] = 255
                else:
                    mask[i:i+n, j:j+n] = 0
        toRemove = []
        for i in range(0, rows, n):
            for j in range(0, cols, n):
                if (i-n<0 or j-n<0 or i+n+1>rows or j+n+1>rows):
                    toRemove.append((i, j))
                elif (mask[i+1, j+1]==0) and (mask[i+n+1, j+1]==255 or mask[i-n+1, j+1]==255 or mask[i+1, j-n+1]==255 or mask[i+1, j+n+1]==255):
                    toRemove.append((i, j))
        for element in toRemove:
            i, j = element[0], element[1]
            mask[i:i+n, j:j+n] = 255
        return mask

    def enhance(self, fpImg, mskImg):
        mskImg2 = self.createMask(fpImg)
        ofDetector = OfDetector()
        ofMat, ofImg = ofDetector.detect(fpImg, mskImg)
        gaborFilterBank = GaborFilterbank()
        enhImg = gaborFilterBank.filter(fpImg, ofImg, mskImg2)
        return enhImg

#-----------------------------
# if __name__ == "__main__":
#     img = cv2.imread("1_1.bmp", cv2.IMREAD_GRAYSCALE)
#     binImg = Binarizer.binarize(img)
#     segmentator = FpSegmentator()
#     img = segmentator.segment(img)
#     enhancer = FpEnhancer()
#     enhImg = enhancer.enhance(img, np.zeros(img.shape))
#     cv2.imshow("binary", enhImg)
#     cv2.waitKey()
#     cv2.destroyAllWindows()

#-----------------------------

