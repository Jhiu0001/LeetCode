# -*- coding: utf-8 -*-
"""
Created on Sun May 23 14:13:15 2021

@author: James Hiu
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        #Initize some variables
        total=m+n #maximum number of times to run while loop
        i=0 #initialize the while loop counter
        n_pos=0 #inititlize the starting position of nums2
        
        #We are asked to modify the nums1 list in place, there are 4 scenarios
        while i <(total):
            #SCENARIO_1
            #nums2 is empty or 
            #we have inserted the last element of nums2 into nums1
            if n_pos==n:
                #We will exit the while loop early and return nums1
                return nums1
            #SCENARIO_2
            #The number in position nums2[n_pos] is less than the element at nums1[i]
            #we will insert the nums2 number into the nums1 list and update our trackers
            elif nums2[n_pos]<=nums1[i]:
                #the number is inserted into nums1 at index i
                nums1.insert(i, nums2[n_pos])
                #we know nums1 has zero elements at the end to accomodate nums2
                #we pop out one of the zeros, keeping the length of nums1 the same
                nums1.pop()
                #we are now interested in the next number in nums2
                n_pos+=1
            #SCENARIO_3
            #The number in position nums2[n_pos] is greater than the element at nums1[i].
            #However, we have are not finished with numbers in the nums1 list yet, m>1
            elif nums2[n_pos]>nums1[i] and m>0:
                #in this scenario we reduced the number of "non-filler" elements in nums1 by one
                m-=1
            #SCENARIO_4
            #Similar to scenario 3, but this time we have gone through all the numbers in the nums1 list.
            #We have to replace the zeroes and update our trackers similar to scenario 2.
            elif nums2[n_pos]>nums1[i] and m==0:
                #the number is inserted into nums1 at index i
                nums1.insert(i, nums2[n_pos])
                #we pop out zeroes from the end of the list
                nums1.pop()
                #we are now interested in the next number on the list, nums2
                n_pos+=1                    
            
            #in scenarios #2,3 & 4 we continue to move through the nums1 list, increasing i by 1.
            i+=1
        
        #returned the modified list, nums1
        return nums1

