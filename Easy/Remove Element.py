# -*- coding: utf-8 -*-
"""
Created on Mon May 17 23:54:45 2021

@author: James Hiu
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        #Exception handling - If the list is empty, the lenght of the list is 0
        if len(nums)==0:
            return 0
        
        #We want to loop through the list backwards
        #To start we test the last element in the list, if it is equal to the target value
        #If it is equal to the target we toss out that element until a non-target value is reached,
        #or until the length of the list is 0.
        while nums[-1]==val:
            nums.pop()
            if len(nums)==0:
                return 0
        
        #Step 2
        #We continue to loop through the list backwards
        for i in reversed(range(len(nums))):
            #In the first iteration (last element in the list) do nothing "continue"
            if i==len(nums)-1:
                continue
            #As we move towards the first element in the list
            #Compare the previous element (i+1) with the target value
            #If the element in position i+1 matches the target, remove it
            elif nums[i+1]==val:
                nums.pop(i+1)
        
        #Step 3
        #Check the first element in the list if it matches the target, remove it
        if nums[0]==val:
            nums.pop(0)       
        
        #Step 4
        #return the length of the list
        return len(nums)    

