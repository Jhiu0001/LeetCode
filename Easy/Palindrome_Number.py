# -*- coding: utf-8 -*-
"""
Created on Thu May 13 23:27:07 2021

@author: James Hiu
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        #Convert the number to a string, reverse the string and store it in a second variable        
        x=str(x)
        x2=x[::-1]
        
        #If the two numbers are equal to each other, it is a palindrome!
        if x==x2:
            return True
        else:
            return False

