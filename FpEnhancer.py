import cv2
import numpy as np
import FpSegmentator
from OfDetector import OfDetector
from GaborFilterbank import GaborFilterbank
from FpSegmentator import FpSegmentator

#-----------------------------
class FpEnhancer:
    def createMask(self, segmentedImg, n = 16):
        rows, cols = segmentedImg.shape
        mask = np.zeros(segmentedImg.shape, dtype = np.uint8)
        black = np.zeros((n, n), dtype = np.uint8)
        for i in range(0, rows, n):
            for j in range(0, cols, n):
                block = img[i:i+n, j:j+n]
                temp = black==block
                if temp.all():
                    mask[i:i+n, j:j+n] = 255
                else:
                    mask[i:i+n, j:j+n] = 0
        return mask
    
    def enhance(self, fpImg, mskImg):
<<<<<<< HEAD
        print("Stub - Fingerprint Enhancement")                 #stub
        print("   Input - a fingerprint image (gray-scale)")    #stub
        print("   Input - a mask image (region-of-interest)")   #stub
        print("   Output - an enhanced image")                  #stub
        mskImg2 = self.createMask(fpImg)
=======
        fpImg = np.where(mskImg==1.0, fpImg, 255)
>>>>>>> origin/master
        ofDetector = OfDetector()
        ofMat, ofImg = ofDetector.detect(fpImg, mskImg)
        gaborFilterBank = GaborFilterbank()
        enhImg = gaborFilterBank.filter(fpImg, ofImg, mskImg2)
        return enhImg

#-----------------------------
if __name__ == "__main__":
    img = cv2.imread("1_1.bmp", cv2.IMREAD_GRAYSCALE)
    binImg = Binarizer.binarize(img)
    cv2.imshow("binary", binImg)
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------
