import cv2
import numpy as np
import math
import time
#from MnExtractor import *

#-----------------------------
class MnMatcher:
    def listSwap(self, list1, list2):
        temp = list1
        list1 = list2
        list2 = temp
        return list1, list2
    
    def translateAllPoints(self, index1, index2, list1, list2):
        delta_x = list2[index2][0] - list1[index1][0] 
        delta_y = list2[index2][1] - list1[index1][1] 
        translated_point_list = []
        for i in range(len(list1)):
            new_x, new_y = self.translation(list1[i][0], list1[i][1], delta_x, delta_y)
            translated_point_list.append([new_x, new_y])
            
        return translated_point_list

    def translation(self, x1,y1,delta_x, delta_y):
        x1 = x1 + delta_x
        y1 = y1 + delta_y
        return x1, y1

    def allAboutRotations(self, index1, index2, list1, list2, index_of_rotation_pts):


        # 1. translate every input points to 0,0
        all_input_pts_at_originate = self.translatePointsToOrigin(index_of_rotation_pts,list1)

        # 1.2 translate every given points to 0,0
        all_given_pts_at_originate = self.translatePointsToOrigin(index_of_rotation_pts,list2)
        
        # 2. find angle
        rotation_angle = self.findAngle(all_input_pts_at_originate[index1][0],
                                   all_input_pts_at_originate[index1][1],
                                   all_given_pts_at_originate[index2][0],
                                   all_given_pts_at_originate[index2][1])
        if(rotation_angle == 1):
            return 0
        # 3. rotate
        all_original_rotated_pts = self.rotateAllPoints(rotation_angle, all_input_pts_at_originate)


        # 4. verify rotation
        # pointsVerification(input, given, acceptable radius)
        accuracy, error_rate = self.pointsVerification(all_original_rotated_pts,
                                                 all_given_pts_at_originate,
                                                 10)
        if(accuracy > 0.8 and error_rate < 0.2):
            return accuracy
        return 0
        '''
        if(all_original_rotated_pts == all_given_pts_at_originate):
            print("=======================")
            print("======== TRUE =========")
            print("=======================")
            return 1
            
        return 0
        '''
        
    def findAngle(self, x1,y1,x2,y2):
        #https://www.wikihow.com/Find-the-Angle-Between-Two-Vectors
        #print("x1: ",x1,"| y1: ",y1,"| x2: ",x2,"| y2: ",y2,"|")
        
        uv = (x1 * x2) + (y1 * y2)
        __u__ = (x1**2 + y1**2)**0.5
        __v__ = (x2**2 + y2**2)**0.5

        if(( __u__ * __v__) == 0):
            return 1

        
        #print("uv: ",uv)
        #print("u: ", __u__)
        #print("v: ", __v__)
        #print("cos0: ", uv / ( __u__ * __v__))
        cosSeta = uv / ( __u__ * __v__)
        if(cosSeta > 1 or cosSeta < -1):
            cosSeta = 1
        angle = math.acos(cosSeta) # / math.pi * 180
        

        #angle = (math.pi * 2) - angle
        angle = (math.pi * 2) - (angle % (math.pi * 2))
        #print("rotation angle: ", (angle / math.pi * 180))
        return angle

    def translatePointsToOrigin(self, index_of_rotation_pts , list1):
        pts_at_origin = []
        for i in range(len(list1)):
            new_x, new_y = self.translation(list1[i][0],list1[i][1],list1[index_of_rotation_pts][0] * -1, list1[index_of_rotation_pts][1] * -1)
            pts_at_origin.append([new_x, new_y])

        #print("translate to origin: ",pts_at_origin)
        #print()
        
        return pts_at_origin
        

    def rotateAllPoints(self, angle, list1):
        rotated_pts = []
        #print("cos: ", round(math.cos(angle)))
        #print("sin: ", round(math.sin(angle)))
        cos_value = (math.cos(angle))
        sin_value = (math.sin(angle))
        #print("cos: ", cos_value)
        #print("sin: ", sin_value)
        for i in range(len(list1)):
            new_x = round((cos_value * list1[i][0]) + (sin_value * -1 * list1[i][1]))
            new_y = round((sin_value * list1[i][0]) + (cos_value * list1[i][1]))
            rotated_pts.append([new_x, new_y])

        #print("after rotate : ", rotated_pts)
        #print()

        return rotated_pts


    def pointsVerification(self, input_pts, given_pts,radius):
        total_given_pts = len(given_pts)
        total_input_pts = len(input_pts)
        match = 0
        not_match = 0
        '''
        for i in range(len(input_pts)):
            if(input_pts[i] in given_pts):
                match += 1
                given_pts.remove(input_pts[i])
            else:
                not_match += 1
        '''
        #with radius
        never_meet = 1
        for i in range(len(input_pts)):
            for j in range(len(given_pts)):
                if((input_pts[i][0] + radius >= given_pts[j][0] and given_pts[j][0] >= input_pts[i][0] - radius)
                   and
                   (input_pts[i][1] + radius >= given_pts[j][1] and given_pts[j][1] >= input_pts[i][1] - radius)):
                    match += 1
                    #print("POP:",given_pts.pop(j))
                    never_meet = 0
                    break
                
            if(never_meet == 1):
                not_match += 1
            else:
                never_meet = 1
            
        accuracy = match/total_input_pts
        error_rate = not_match/total_input_pts
        #print("ACCURACY: ", accuracy)
        #print("ERROR RATE: ", error_rate)
        return accuracy,error_rate


    ################ SAMPLING #####################################

    def samplingPoint(self, list1, size):
        step_size = int(len(list1)/size)
        sampling_set = []
        for i in range(0,10):
            sampling_set.append(list1[i])

        for i in range(100,110):
            sampling_set.append(list1[i])
        print("SAMPLING", sampling_set)
        return sampling_set

    def createSample4Part(self, list1, list2, sample_size):
        from_each_population = round(sample_size / 4)
        sample_list = []
        for i in range(from_each_population):
            sample_list.append(list1[i])
            
        for i in range(len(list1)- from_each_population, len(list1)):
            sample_list.append(list1[i])

        for i in range(from_each_population):
            sample_list.append(list2[i])
            
        for i in range(len(list2)- from_each_population, len(list2)):
            sample_list.append(list2[i])

        print("sample: ", sample_list)
        return sample_list

    def createSample2Part(self, list1, list2, sample_size):
        from_each_population = round(sample_size / 2)
        sample_list = []
        for i in range(from_each_population):
            sample_list.append(list1[i])
        for i in range(from_each_population):
            sample_list.append(list2[i])

        print("sample: ", sample_list)
        return sample_list

    def normalSampling(self, list1, size):
        sample_list = []
        for i in range(size):
            sample_list.append(list1[i])
        return sample_list

    ####################################################################################

    def match(self, mnSet1, mnSet2):
        print("Stub - Minutia Matching")                    #stub
        print("   Input - a set of minutiae (template)")    #stub
        print("   Input - a set of minutiae (input)")       #stub
        print("   Output - similarity score")               #stub

        input_point_list = [[0,3],[0,0],[3,0]] #### mnSet1
        given_point_list = [[6,6],[3,6],[3,3]] #### mnSet2
        
        if(len(input_point_list) > len(given_point_list)):
            print("swap list")
            input_point_list, given_point_list = self.listSwap(input_point_list,given_point_list)
        start_time = time.time()
        answer = 0
        for i in range(len(input_point_list)):
            print("###########",i,"############")
            for j in range(len(given_point_list)):
                translated_points = self.translateAllPoints(i,j,input_point_list,given_point_list)     
                for k in range(len(translated_points)):
                    for l in range(len(given_point_list)):   
                        similarity = self.allAboutRotations(k,l,translated_points,given_point_list, i)
                        if(similarity > 0.75):
                            answer = 1
                        if(answer == 1):
                            break
                    if(answer == 1):
                        break
                if(answer == 1):
                    break
            if(answer == 1):
                break    
        if(answer == 1):
            print("-------------")
            print("    MATCH   ")
            print("-------------")
        else:
            print("-------------")
            print("  NOT MATCH")
            print("-------------")
        print("--TIME----------------------------")
        print("    %s seconds " % (time.time() - start_time))
        print("----------------------------------")
                                                            #stub
        return similarity                                   #stub
    
#-----------------------------
if __name__ == "__main__":
    img = cv2.imread("img/1_1.bmp", cv2.IMREAD_GRAYSCALE)
    #ae = MnExtractor()
    #mnSet = ae.extract(img)

    ae2 = MnMatcher()
    mnSet = []
    s = ae2.match(mnSet, mnSet)
    print(s)
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------
