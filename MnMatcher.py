import cv2
import numpy as np
import math
from MnExtractor import *

#-----------------------------
class MnMatcher:
    def match(self, mnSet1, mnSet2):
        print("Stub - Minutia Matching")                    #stub
        print("   Input - a set of minutiae (template)")    #stub
        print("   Input - a set of minutiae (input)")       #stub
        print("   Output - similarity score")               #stub
        similarity = 0.75                                   #stub
        return similarity                                   #stub
    
#-----------------------------
if __name__ == "__main__":
    img = cv2.imread("1_1.bmp", cv2.IMREAD_GRAYSCALE)
    mnSet = MnExtractor.extract(img)
    s = MnMatcher.match(mnSet, mnSet)
    print(s)
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------
