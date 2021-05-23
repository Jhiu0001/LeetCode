# -*- coding: utf-8 -*-
"""
Created on Sat May 22 22:47:45 2021

@author: James Hiu
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        #The trick to solving this problem is to realize the step climber must land on a step
        #two steps before or one step before the top step.
        
        #For example, step 2 can be reached directly from the ground or from step 1 (2 ways). 
        #Step 3 can be reached from step 1 or step 2 - There are two ways to reach step 2, 
        #one way to reach step 1, meaning there are 3 ways to reach step 3.
        #Extrapolating this pattern step "N" can be reach from step "n-1" and step "n-2".
        
        #Those familiar with this pattern will note that this sequence has a name, a Fibonacci number.
        
        #Special Cases
        #There is 1 way to ascend a 1 step ladder or stand on the ground
        if n==(0 or 1):
            return 1
        
        #Step 1
        #Because of our special case, initiate step 0 and step 1 as 1-way and 1-way
        two_below=1
        one_below=1
        
        #Step 2
        #we calculate the Fibonacci number on step 2,3,4 all the way up to step N which we are provided.
        for i in range(2,n+1):
            num_ways=two_below+one_below
            two_below=one_below
            one_below=num_ways
        
        return num_ways

