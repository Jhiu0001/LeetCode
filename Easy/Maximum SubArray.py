# -*- coding: utf-8 -*-
"""
Created on Thu May 20 18:14:06 2021

@author: James Hiu
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Initialize 2 variables
        total=0
        max_total=0        
        
        # we will be iterating through the list to find a solution
        for i in range(len(nums)):
            #if the adding a number to our list will make the total negative
            #reset the total to 0
            if total+nums[i]<0:
                total=0
            else:
            #otherwise if add the number to the total
                total+=nums[i]
                #check if our new total is the largest total we have seen
                if total>max_total:
                    #if true, set max_total equal to total
                    max_total=total
        
        #Special cases
        #What if all elements in the list are zero?
        #We initiaized an answer greater than the least negative number
        #In this scenario, check if max_total equals zero then take a single number as the answer
        #namely the smallest negative number.
        
        #What if list elements contain only negative numbers and zero(es)?
        #the logic also holds
        if max_total==0:
            return max(nums)
        
        #return the max_total if we are not dealing with special cases.
        else:
            return max_total

