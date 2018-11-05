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
        self.segmentator = FpSegmentator.FpSegmentator(8)
        #constructing FpEnhancer
        self.enhancer = FpEnhancer.FpEnhancer()
        #constructing MnExtractor
        self.extractor = MnExtractor.MnExtractor()
        #constructing MnMatcher
        self.matcher = MnMatcher.MnMatcher()

    def match(self, fpImg1, fpImg2):
        segmentedFpImg1 = self.segmentator.segment(fpImg1)
        enhancedFpImg1 = self.enhancer.enhance(segmentedFpImg1, np.ones(segmentedFpImg1.shape))
        mnSet1 = self.extractor.extract(enhancedFpImg1)

        segmentedFpImg2 = self.segmentator.segment(fpImg2)
        enhancedFpImg2 = self.enhancer.enhance(segmentedFpImg2, np.ones(segmentedFpImg2.shape))
        mnSet2 = self.extractor.extract(enhancedFpImg2)

        return self.matcher.match(mnSet1, mnSet2)

#-----------------------------

if __name__ == "__main__":
    #read fingerprint image 1
    fpImg1 = cv2.imread("FP DB (subset)/1_1.bmp", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("fp1", fpImg1);

    #read fingerprint image 2
    fpImg2 = cv2.imread("FP DB (subset)/1_2.bmp", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("fp2", fpImg2);

    #match two fingerprint images
    fpMatcher = FpMatcher()
    similarity = fpMatcher.match(fpImg1, fpImg2)
    print("Similary = ", similarity)

    cv2.waitKey()
    cv2.destroyAllWindows()
#-----------------------------
