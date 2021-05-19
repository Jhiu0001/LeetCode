# -*- coding: utf-8 -*-
"""
Created on Tue May 18 22:12:56 2021

@author: James Hiu
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        #look for a sub-string in a string
        #Question requirement, if no substring is provided (needle), return 0
        if len(needle)==0:
            return 0
        
        #Step 2
        #Use the index function to identify the first occurrance of the substring in the string
        #If the string does not contain the substring return -1 as requested
        try:
            x=haystack.index(needle)
        except:
            x=-1
        
        return x

