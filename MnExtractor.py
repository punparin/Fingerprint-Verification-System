import cv2
import numpy as np
import Binarizer
import Skeletonizer
#-----------------------------
#minutiae types
M_TYPE_UNKNOWN      = 0
M_TYPE_ENDPOINT     = 1
M_TYPE_BIFURCATION  = 2
#-----------------------------
class MnExtractor:
    def __init__(self):
        #constructing Binarizer
        self.binarizer = Binarizer.Binarizer()
        #constructing Skeletonizer
        self.skeletonizer = Skeletonizer.Skeletonizer()

    def calculate_cn(self, img, i, j):
        l = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
        total = 0
        for k in range(len(l) - 1):
            row = i + l[k][0]
            col = j + l[k][1]
            next_row = i + l[k + 1][0]
            next_col = j + l[k + 1][1]
            total += abs(img[row, col] / 255 - img[next_row, next_col] / 255)
        return total / 2

    def isLeftBoundary(self, img, i, j):
        rows, cols = img.shape
        isBound = True
        for k in range(j - 1, -1, -1):
            if img[i, k] == 0:
                isBound = False
                break
        return isBound

    def isRightBoundary(self, img, i, j):
        rows, cols = img.shape
        isBound = True
        for k in range(j + 1, cols):
            if img[i, k] == 0:
                isBound = False
                break
        return isBound

    def isBoundary(self, img, i, j):
        if self.isLeftBoundary(img, i, j) or self.isRightBoundary(img, i, j):
            return True
        return False

    def extract(self, enhancedImg):
        rows, cols = enhancedImg.shape
        binImg = self.binarizer.binarize(enhancedImg)
        skeletonImg = self.skeletonizer.skeletonize(binImg)
        mnSet = []
        count = 0
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if(skeletonImg[i, j] == 0):
                    cn = self.calculate_cn(skeletonImg, i, j)
                    if cn == 1:
                        mnSet.append([i, j, M_TYPE_ENDPOINT])
                    elif cn == 3 and not self.isBoundary(enhancedImg, i, j):
                        mnSet.append([i, j, M_TYPE_BIFURCATION])
        return mnSet

#-----------------------------
if __name__ == "__main__":
    from gabor import GaborEnhance
    from FpSegmentator import FpSegmentator
    from FpEnhancer import FpEnhancer

    # img = cv2.imread("FP DB (subset)/1_1.bmp", cv2.IMREAD_GRAYSCALE)
    # cv2.imshow("Original image", img)

    # segmentator = FpSegmentator(8)
    # segmentedImg = segmentator.segment(img)
    # cv2.imshow("Segmented image", segmentedImg)

    # enhance = GaborEnhance()
    # enhancedImg = enhance.enhanceImage(segmentedImg, 16)
    # cv2.imshow("Enhanced image", enhancedImg)

    # mnSet = MnExtractor().extract(enhancedImg)
    # print(len(mnSet))
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    for i in range(1, 5):
        for j in range(1, 5):
            img = cv2.imread("FP DB (subset)/" + str(i) + "_" + str(j) + ".bmp", cv2.IMREAD_GRAYSCALE)
            segmentator = FpSegmentator(8)
            segmentedImg = segmentator.segment(img)

            enhancer = FpEnhancer()
            enhancedImg = enhancer.enhance(segmentedImg, np.ones(img.shape))

            mnSet = MnExtractor().extract(enhancedImg)
            print(len(mnSet))

#-----------------------------
