import cv2
import numpy as np

#-----------------------------
class Binarizer:
    def binarize(self, fpImg):
        print("Stub - Binarization")                            #stub
        print("   Input - a fingerprint image (gray-scale)")    #stub
        print("   Output - a binary image")                     #stub
        binImg = fpImg                                          #stub
        return binImg
        
#-----------------------------
if __name__ == "__main__":
    img = cv2.imread("1_1.bmp", cv2.IMREAD_GRAYSCALE)
    binImg = Binarizer.binarize(img)
    cv2.imshow("binary", binImg)
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------
