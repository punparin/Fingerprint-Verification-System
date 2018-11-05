import cv2
import numpy as np
import math

#-----------------------------
class FpSegmentator:
    def __init__(self, bs = 8):
        self.blockSize = bs

    def segment(self, fpImg):
        segmentedImg = fpImg
        maskImg = fpImg
        # kernely = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
        # kernelx = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])

        #sobel
        kernely = np.array([[-3,-10,-3],[0,0,0],[3,10,3]])
        kernelx = np.array([[-3,0,3],[-10,0,10],[-3,0,3]])

        edges_x = cv2.filter2D(fpImg, cv2.CV_8U,kernelx)
        edges_y = cv2.filter2D(fpImg, cv2.CV_8U,kernely)

        rows, cols, *ch = maskImg.shape
        total = 0
        sd = 0
        size = self.blockSize**2

        for row in range(0,rows, self.blockSize):
            for col in range(0,cols, self.blockSize):
                try:
                    for r in range(row,row + self.blockSize):
                        for c in range(col,col + self.blockSize):
                            total += edges_x[r,c]
                    for r in range(row,row + self.blockSize):
                        for c in range(col,col + self.blockSize):
                            sd += (edges_x[r,c] - (total//size))**2
                    x_sd = math.sqrt(sd//self.blockSize)

                    for r in range(row,row + self.blockSize):
                        for c in range(col,col + self.blockSize):
                            total += edges_y[r,c]
                    for r in range(row,row + self.blockSize):
                        for c in range(col,col + self.blockSize):
                            sd += (edges_y[r,c] - (total//size))**2
                    y_sd = math.sqrt(sd//self.blockSize)

                    if  x_sd < 200 or y_sd < 380: #420, 700
                        for r in range(row,row+16):
                            for c in range(col,col+16):
                                segmentedImg[r,c] = 255
           
                    total = 0
                    sd = 0
                except IndexError as ie:
                    pass
        return segmentedImg

#-----------------------------

# if __name__ == "__main__":
#     img = cv2.imread("FP DB (subset)/6_1.bmp", cv2.IMREAD_GRAYSCALE)
#     segmentator = FpSegmentator(8)
#     segmentedImg = segmentator.segment(img)
#     cv2.imshow("segment", segmentedImg)
#     cv2.waitKey()
#     cv2.destroyAllWindows()

#-----------------------------
