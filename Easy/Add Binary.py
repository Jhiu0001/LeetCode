# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:50:11 2021

@author: James Hiu
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        #initialize two numbers to zero
        num1=0
        num2=0

        #We need to convert the binary number given as a string to an integer number
        #it is calculated as the sum of  (1 or 0)x2^0 + (1 or 0)x2^1 + (1 or 0)x2^2, etc.
        #Also note that binary numbers are calculated right to left, just like integers -
        #the greatest magnitude integer is left most, position string[0]
        for i in range(len(a)):
            num1+=int(a[i])*(2**(len(a)-1-i))

        #We convert binary number "b" the exact same way
        for i in reversed(range(len(b))):
            num2+=int(b[i])*(2**(len(b)-1-i))        

        #Return the answer using the bin function to convert the interger sum to binary
        #Binarys numbers are returned as 0bXXXXX, the [2:] will truncate the "0b" chracters
        return bin(num1+num2)[2:]

