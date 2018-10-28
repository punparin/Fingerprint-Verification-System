import cv2
import numpy as np

#-----------------------------
class FpSegmentator:
    def __init__(self, bs = 16):
        self.blockSize = bs
        
    def segment(self, fpImg):  
        print("Stub - Fingerprint segmentation")                #stub
        print("   Input - a fingerprint image")                 #stub
        print("   Output - a segmented image")                  #stub
        print("   Output - a mask image (region-of-interest)")  #stub
        segmentedImg = fpImg                                    #stub       
        maskImg = fpImg                                         #stub        
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
