import cv2
import numpy as np
from GaborFilter import GaborFilter

#-----------------------------
class GaborFilterbank:
    def __init__(self):
        self.kernels = {}
        orientations = [0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5]
        for orientation in orientations:
            self.kernels[orientation] = GaborFilter(10, orientation, 8)

    def filter(self, fpImg, ofImg, mskImg):
        img = fpImg
        n = 16
        rows, cols = img.shape
        orientations = np.zeros((rows//n, cols//n), dtype = np.float32)
        for i in range(orientations.shape[0]):
            for j in range(orientations.shape[1]):
                orientations[i, j] = ofImg[i*n+1, j*n+1]
        block_rows = n
        block_cols = n
        padding = 6
        for i in range(0, rows, n):
            if i-padding>0:
                i1 = i-padding
            else:
                i1 = 0
            if i+padding+n<rows:
                i2 = i+n+padding
            else:
                i2 = rows
            for j in range(0, cols, n):
                if j-padding>0:
                    j1 = j-padding
                else:
                    j1 = 0
                if j+padding+n<cols:
                    j2 = j+n+padding
                else:
                    j2 = cols
                block = img[i1:i2, j1:j2]
                orientation = orientations[i//n, j//n]
                gabor = self.kernels[orientation]
                img[i:i+n, j:j+n] = gabor.filter(block)[i-i1:i-i1+n, j-j1:j-j1+n]

        img = np.where(mskImg==0, img, 255)
        return img

#-----------------------------
if __name__ == "__main__":
    pass

#-----------------------------
