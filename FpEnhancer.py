import cv2
import numpy as np
import FpSegmentator
import OfDetector
import GaborFilterbank

#-----------------------------
class FpEnhancer:
    def enhance(self, fpImg, mskImg):
        print("Stub - Fingerprint Enhancement")                 #stub
        print("   Input - a fingerprint image (gray-scale)")    #stub
        print("   Input - a mask image (region-of-interest)")   #stub
        print("   Output - an enhanced image")                  #stub
        enhImg = fpImg                                          #stub
        return enhImg
        
#-----------------------------
if __name__ == "__main__":
    img = cv2.imread("1_1.bmp", cv2.IMREAD_GRAYSCALE)
    binImg = Binarizer.binarize(img)
    cv2.imshow("binary", binImg)
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------

