# -*- coding: utf-8 -*-
"""
Created on Thu May 13 15:12:42 2021

@author: James Hiu
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        'Iterate through the array looking for a pair of numbers that sum to the target'
        for i in range(len(nums)):
            'taking the i-th number in the array, calculate the needed number, target2'
            target2=target-nums[i]
            'Check if target2 is also in the array'
            'A element in the num array can only be used once,'
            'therefore only the array elements coming after the i-th element are checked'
            if target2 in nums[i+1:]:
                'if found - we calculate the index position of target2 in the nums array'
                j=(nums[i+1:].index(target2))+(i+1)                
                'return the answer'
                return [i,j]
