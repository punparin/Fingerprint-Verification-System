import cv2
import numpy as np
import FpSegmentator
from OfDetector import OfDetector
from GaborFilterbank import GaborFilterbank

#-----------------------------
class FpEnhancer:
    def enhance(self, fpImg, mskImg):
<<<<<<< HEAD
        print("Stub - Fingerprint Enhancement")                 #stub
        print("   Input - a fingerprint image (gray-scale)")    #stub
        print("   Input - a mask image (region-of-interest)")   #stub
        print("   Output - an enhanced image")                  #stub
<<<<<<< HEAD
        mskImg2 = self.createMask(fpImg)
=======
        fpImg = np.where(mskImg==1.0, fpImg, 255)
>>>>>>> origin/master
=======
        fpImg = np.where(mskImg==1.0, fpImg, 255)
>>>>>>> parent of 53a8350... created mask
        ofDetector = OfDetector()
        ofMat, ofImg = ofDetector.detect(fpImg, mskImg)
        gaborFilterBank = GaborFilterbank()
        enhImg = gaborFilterBank.filter(fpImg, ofImg, mskImg)
        return enhImg

#-----------------------------
if __name__ == "__main__":
    img = cv2.imread("1_1.bmp", cv2.IMREAD_GRAYSCALE)
    binImg = Binarizer.binarize(img)
    cv2.imshow("binary", binImg)
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------

