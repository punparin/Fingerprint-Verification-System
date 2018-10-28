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
        #constructing Skeletonizer
        
    def extract(self, enhancedImg):
        print("Stub - Minutia Extraction")                      #stub
        print("   Input - an enhanced fingerprint image")       #stub
        print("   Output - a set of minutiae")                  #stub
        mnSet = [[ 10,  25, M_TYPE_ENDPOINT], \
                 [120,  78, M_TYPE_BIFURCATION], \
                 [104, 125, M_TYPE_BIFURCATION]]    #stub       
        return mnSet
              
#-----------------------------
if __name__ == "__main__":
    img = cv2.imread("1_1.bmp", cv2.IMREAD_GRAYSCALE)
    mnSet = MnExtractor.extract(img)
    print(mnSet)
    print(len(mnSet))
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------
