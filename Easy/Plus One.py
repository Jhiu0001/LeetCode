# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:39:06 2021

@author: James Hiu
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        #Convert the list of numbers into a string and join it (e.g. [9,9] becomes '99')       
        str_num=''.join([str(digits[i]) for i in range(len(digits))])
        
        #Convert the string to an integer and add 1 to it (e.g. '99'-->99+1 )
        num=int(str_num)+1
        
        #Convert the answer back into list format (e.g. 100 -->[1,0,0])
        ans=[int(d) for d in str(num)]
        
        #Provide the answer
        return ans

