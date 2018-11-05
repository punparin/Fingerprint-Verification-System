import cv2
import numpy as np

#-----------------------------
class Skeletonizer:
    def count_black_neighbour(self, img, i, j):
        count = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                if k == 0 and l == 0:
                    continue
                elif img[i + k][j + l] == 0:
                    count += 1
        return count

    def count_transition(self, img, i, j):
        l = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
        count = 0
        for k in range(1, len(l)):
            row = i + l[k][0]
            col = j + l[k][1]
            prev_row = i + l[k - 1][0]
            prev_col = j + l[k - 1][1]
            if img[prev_row, prev_col] == 255 and img[row, col] == 0:
                count += 1
        return count

    def areConPixelsWhite(self, img, i, j, isOdd):
        if isOdd:
            if img[-1, 0] == 255 or img[0, 1] == 255 or img[1, 0] == 255:
                return True
            elif img[0, 1] == 255 or img[1, 0] == 255 or img[0, -1] == 255:
                return True
        else:
            if img[-1, 0] == 255 or img[0, 1] == 255 or img[0, -1] == 255:
                return True
            elif img[-1, 0] == 255 or img[1, 0] == 255 or img[0, -1] == 255:
                return True
        return False

    def skeletonize(self, binImg):
        rows, cols = binImg.shape
        count = 1
        isDeleting = True
        while isDeleting:
            isDeleting = False
            for i in range(1, rows - 1):
                for j in range(1, cols - 1):
                    if binImg[i][j] == 0:
                        if 2 <= self.count_black_neighbour(binImg, i, j) <= 6:
                            if self.count_transition(binImg, i, j) == 1:
                                if self.areConPixelsWhite(binImg, i, j, count % 2):
                                    binImg[i][j] = 255
                                    isDeleting = True
            count += 1
        return binImg

#-----------------------------
# if __name__ == "__main__":
#     img = cv2.imread("FP DB (subset)/fingerprint.bmp", cv2.IMREAD_GRAYSCALE)
#     from Binarizer import Binarizer
#     binImg = Binarizer().binarize(img)
#     skeletonImg = Skeletonizer().skeletonize(binImg)
#     cv2.imshow("skeleton", skeletonImg)
#     # cv2.imwrite("skeleton.bmp", skeletonImg)
#     cv2.waitKey()
#     cv2.destroyAllWindows()

#-----------------------------

