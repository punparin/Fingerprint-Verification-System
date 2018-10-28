import cv2
import numpy as np
import math

#-----------------------------
class FpSegmentator:
    def __init__(self, bs = 8):
        self.blockSize = bs
        
    def segment(self, fpImg):  
        print("Stub - Fingerprint segmentation")                #stub
        print("   Input - a fingerprint image")                 #stub
        print("   Output - a segmented image")                  #stub
        print("   Output - a mask image (region-of-interest)")  #stub
        segmentedImg = fpImg                                    #stub       
        maskImg = fpImg                                         #stub  
        segmentedImg = fpImg                                  
        maskImg = fpImg                         
        rows, cols, *ch = maskImg.shape
        total = 0
        sd = 0
        size = self.blockSize**2

        for row in range(0,rows, self.blockSize):
            for col in range(0,cols, self.blockSize):
                try:
                    for r in range(row,row + self.blockSize):
                        for c in range(col,col + self.blockSize):
                            total += maskImg[r,c]
                    for r in range(row,row + self.blockSize):
                        for c in range(col,col + self.blockSize):
                            sd += (maskImg[r,c] - (total//size))**2
                    sd = math.sqrt(sd//self.blockSize)
                    if(total//size < 63) and sd < 160:
                        for r in range(row,row + self.blockSize):
                            for c in range(col,col + self.blockSize):
                                segmentedImg[r,c] = 0
                                
                    total = 0
                    sd = 0
                except IndexError as ie:
                    pass
        return segmentedImg, maskImg      
   
#-----------------------------

if __name__ == "__main__":
    img = cv2.imread("1_1.bmp", cv2.IMREAD_GRAYSCALE)
    segmentator = FpSegmentator(16)
    maskImg = segmentator.segment(img)
    cv2.imshow("segment", maskImg)
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------
