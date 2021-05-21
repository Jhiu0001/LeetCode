# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:41:16 2021

@author: James Hiu
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #Seperate the string using space as the delimiter
        arr=s.split(' ')
    
        #Initiate the counter, we will be looping through the list backwards
        i=len(arr)-1
    
        #Starting from the end of the list, if the list item is an empty chracter, remove the list element
        while i>0:
            if arr[i]=="":
                arr.pop()
                i-=1
            #As soon as we reach a non-empty character, stop the while loop
            else:
                i=-1

        #Return the length of the last list item as requested
        return (len(arr[-1]))

