# -*- coding: utf-8 -*-
"""
Created on Thu May 13 21:55:14 2021

@author: James Hiu
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        #Convert the number to a string and reverse the string
        #Multiply negative numbers by -1 and then reverse the string
        if x>0: 
            x2=str(x)[::-1]
        else:
            x2='-'+str(x*-1)[::-1]
        
        #Convert the number back to an integer
        x=int(x2)
        
        #Test that our number is in between the lower and upper bound
        #Return 0 if the reversed number is outside the range as directed
        if x<(-2**31):
            return 0
        elif x>(2**31-1):
            return 0
        else:
            return x

