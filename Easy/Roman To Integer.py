# -*- coding: utf-8 -*-
"""
Created on Fri May 14 14:36:37 2021

@author: James Hiu
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Initiate two variables, we will cumulatively add to our running total
        #"i" is used to track our position as we read our Roman Numeral (RN) string left to right      
        total=0
        i=0
        
        #Recognize that RN numbers are sometimes read two characters at a time (i.e. C,X,I).
        
        #RN numbers ending in "C","X","I" will throw an error if our code checks for corresponding 
        #2-character combinations, attempting to check the next character which does not exist. 
        #I used a try/except data structure to overcome this issue 
        
        #We move through the RN string accruing our total and advancing the index position "i"
        #as we covert 1 or 2 RN character strings into numbers.
        while i < len(s):
        
            if s[i]=='C':
                try:
                    if s[i]+s[i+1]=='CM':
                        total+=900
                        i+=2
                    elif s[i]+s[i+1]=='CD':
                        total+=400
                        i+=2
                    else:
                        total+=100
                        i+=1
                except:
                    total+=100
                    i+=1

            elif s[i]=='X':
                try:
                    if s[i]+s[i+1]=='XC':
                        total+=90
                        i+=2
                    elif s[i]+s[i+1]=='XL':
                        total+=40
                        i+=2
                    else:
                        total+=10
                        i+=1
                except:
                    total+=10
                    i+=1

            elif s[i]=='I':
                try:
                    if s[i]+s[i+1]=='IX':
                        total+=9
                        i+=2
                    elif s[i]+s[i+1]=='IV':
                        total+=4
                        i+=2
                    else:
                        total+=1
                        i+=1
                except:
                    total+=1
                    i+=1

            elif s[i]=='M':
                total+=1000
                i+=1
            elif s[i]=='D':
                total+=500
                i+=1
            elif s[i]=='L':
                total+=50
                i+=1
            elif s[i]=='V':
                total+=5
                i+=1
        
        #Once we have converted the RN string, we return the calculated summation                     
        return total

