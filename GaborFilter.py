import cv2
import numpy as np

#-----------------------------
class GaborFilter:
    def __init__(self, size, orientation, frequency):
        self.gaborFilter = cv2.getGaborKernel((size, size), 3, orientation*np.pi/180, frequency, 4, 0, cv2.CV_32F)

    def filter(self, block):
        filteredImage = cv2.filter2D(block, cv2.CV_8U, self.gaborFilter)
        return filteredImage

#-----------------------------
if __name__ == "__main__":
    pass

#-----------------------------
