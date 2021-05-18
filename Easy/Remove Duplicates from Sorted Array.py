# -*- coding: utf-8 -*-
"""
Created on Mon May 17 22:57:13 2021

@author: James Hiu
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #We are given a sorted integer list and told to remove duplicates in place
        #To solve this problem, we loop through the array backwards
        for i in reversed(range(len(nums))):
            #For the first pass / last element in the list, do nothing "continue"
            if i==len(nums)-1:
                continue
            #As we move towards the first element in the list, compare it with the next number in the list
            #i.e. the number that we just passed
            elif nums[i]==nums[i+1]:
                #if the two numbers are equal we want to delete the element in the i+1 position
                #index position that was passed, as oppose to the index position we are on
                #This is done so the for loop continues to run
                nums.pop(i+1)
        
        #The question asks us to return the length of the array as oppose to the array
        return len(nums)       

