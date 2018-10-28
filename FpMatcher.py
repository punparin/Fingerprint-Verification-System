import cv2
import numpy as np
import FpSegmentator
import FpEnhancer
import MnExtractor
import MnMatcher

#-----------------------------
class FpMatcher:
    def __init__(self):
        #constructing FpSegmentator
        #constructing FpEnhancer
        #constructing MnExtractor
        #constructing MnMatcher
        
    def match(self, fpImg1, fpImg2):
        print("Stub - Fingerprint Matching")                #stub
        print("   Input - a fingerprint image (template)")  #stub
        print("   Input - a fingerprint image (input)")     #stub
        print("   Output - similarity score")               #stub
        similarity = 0.75                                   #stub
        return similarity                                   #stub
        
#-----------------------------

if __name__ == "__main__":
    #read fingerprint image 1
    fpImg1 = cv2.imread("../FP DB1 (train subset)/1_1.bmp", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("fp1", fpImg1);

    #read fingerprint image 2
    fpImg2 = cv2.imread("../FP DB1 (train subset)/1_2.bmp", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("fp2", fpImg2);

    #match two fingerprint images
    fpMatcher = FpMatcher()
    similarity = fpMatcher.match(fpImg1, fpImg2)
    print("Similary = ", similarity)

    cv2.waitKey()
    cv2.destroyAllWindows()
#-----------------------------
