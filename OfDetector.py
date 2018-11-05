import cv2
import numpy as np
import math

#-----------------------------
class OfDetector:
    def computeOrientation(self, block):
        blockGx = cv2.Sobel(block, cv2.CV_32F, 1, 0)
        blockGy = cv2.Sobel(block, cv2.CV_32F, 0, 1)
        vX = 0
        vY = 0
        rows, cols = blockGx.shape
        for u in range(rows):
            for v in range(cols):
                vX+=2*blockGx[u, v]*blockGy[u, v]
                vY+=(blockGx[u, v])**2-(blockGy[u, v])**2
        theta = (np.arctan2(vX, vY)*0.5)
        theta = (theta + np.pi * 0.5) % np.pi
        return math.degrees(theta)+45

    def quantizeOrientation(self, orientation):
        orientations = [0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5]
        if orientation<0:
            orientation+=360
        if orientation>180:
            orientation/=2
        dist = 999
        currentOrientation = 0
        for o in orientations:
            d = abs(o-orientation)
            if d<dist:
                dist = d
                currentOrientation = o
        return currentOrientation
    
    def ridge_estimation(self, img, n):
        rows, cols = img.shape
        orientations = np.zeros((rows//n+1, cols//n+1), dtype = np.float32)
        block_rows = n
        block_cols = n
        for i in range(0, rows, n):
            i2 = i+n
            for j in range(0, cols, n):
                j2 = j+n
                block = img[i:i2, j:j2]
                orientations[i//n, j//n] = self.quantizeOrientation(self.computeOrientation(block))
        return orientations
    
    def detect(self, fpImg, mskImg):
        print("Stub - Orientation Field Detection")             #stub
        print("   Input - a fingerprint image (gray-scale)")    #stub
        print("   Input - a mask image (region-of-interest)")   #stub
        print("   Output - an orientation field (matrix)")      #stub
        print("   Output - an orientation field (image)")       #stub
        n = 16
        img = fpImg
        img = np.where(mskImg==1.0, img, 255)
        rows, cols = img.shape
        yblocks, xblocks = rows//n, cols//n
        orientations = self.ridge_estimation(img, n)
        ofMat = orientations
        ofImg = np.full(img.shape, -1.0)
        for y in range(yblocks):
            for x in range(xblocks):
                ofImg[y*n:(y+1)*n, x*n:(x+1)*n] = ofMat[y, x]
        return ofMat, ofImg                     #stub
        
#-----------------------------
if __name__ == "__main__":
    pass

#-----------------------------
