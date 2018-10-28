import cv2
import numpy as np

#-----------------------------
class Skeletonizer:
    def skeletonize(self, binImg):
        print("Stub - Skeletonization")         #stub
        print("   Input - a binary image")      #stub
        print("   Output - a skeleton image")   #stub
        skeletonImg = binImg                    #stub
        return skeletonImg
    
#-----------------------------
if __name__ == "__main__":
    img = cv2.imread("1_1.bmp", cv2.IMREAD_GRAYSCALE)
    from Binarizer import Binarizer
    binImg = Binarizer.binarize(img)
    skeletonImg = Skeletonizer.skeletonize(binImg)
    cv2.imshow("skeleton", skeletonImg)
    cv2.imwrite("skeleton.bmp", skeletonImg)
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------

