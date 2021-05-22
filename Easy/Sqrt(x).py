# -*- coding: utf-8 -*-
"""
Created on Fri May 21 21:53:47 2021

@author: James Hiu
"""
import math

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        #To calculate the squareroot and truncate the decimal places
        #We use the floor function and then convert our answer to data type, integer.
        return int(math.floor(x**0.5))

