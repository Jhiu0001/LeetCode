# -*- coding: utf-8 -*-
"""
Created on Tue May 18 22:56:50 2021

@author: James Hiu
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        #Step 1
        #Look for special cases
        #If the list is empty or if the first element is equal to the target, return 0
        # (Checking if the first element==target may seem reduntant with our loop below.
        # However if the list is of lenght=1, our while loop will miss this secnario)
        if target<nums[0] or target==nums[0]:
            return 0
        
        #Step 2
        #Check the end point 
        #if the target is equal to the last element, return length(list)-1
        #if the target is greater than the last element, return length (list)
        if target==nums[-1]:
            return len(nums)-1
        elif target>nums[-1]:
            return len(nums)
        
        #Initiate our counter at index zero
        i=0
        
        #Step 3
        #Go through the list checking sequentially, there are 3 possibilities
        while i<len(nums)-1:
            #the number at index position i is equal to the target, return i
            if nums[i]==target:
                return i
            #the number is greater than the number at index position i but less than number at i+1, return i+1
            elif nums[i]<target and nums[i+1]>target:
                return i+1
            #neither of those cases are true, increment the counter
            else:          
                i+=1

