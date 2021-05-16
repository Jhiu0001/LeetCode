# -*- coding: utf-8 -*-
"""
Created on Sat May 15 17:24:40 2021

@author: James Hiu
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #If the string is odd length report False
        if len(s)%2==1:
            return False
        
        #Convert the string to a list so we can iterate through the elements
        arr=list(s)

        #Initiate i to the length of the list, we will be removing open and close bracket pairs
        i=len(arr)
        
        #We use a while loop to toss out bracket pairs in this solution        
        while i>0:
            #the first step is grab the first index position of backet closing characters ),],}
            #if a certain type of bracket does not exist we will assign the -1 index position
            try:
                c1=arr.index(')')
            except:
                c1=-1
            try:
                c2=arr.index('}')
            except:
                c2=-1
            try:   
                c3=arr.index(']')
            except:
                c3=-1

            #In step two we remove all the invalid index positions if a certain type of bracket does not exist
            #If we do not find any close bracket characters, report False (i.e. '((')
            arr2=[c1,c2,c3]
            arr2=list(filter(lambda a: a != -1, arr2))
            if len(arr2)==0:
                return False
            #If two or more close bracket types are found, ) or } or ], take the one that occurs first
            close=min(arr2)
            
            #If the list starts off with a close bracket character then, report False i.e. ' }(()) '
            if close==0:
                return False

            #In the 3rd step, we check if the character right before the close bracket character 
            #is equal to its open bracket pair.
            
            #For example, "{" and ")" will return an error, we must close open brackets from the inside out
            #If we find a valid pair the idea is to delete the pair out of the list, (()) -->(xx)-->()
            if arr[close]==')':
                if arr[close-1]=='(':
                    arr.pop(close)
                    arr.pop(close-1)
                    i-=2
                else:
                    return False
            elif arr[close]=='}':
                if arr[close-1]=='{':
                    arr.pop(close)
                    arr.pop(close-1)
                    i-=2
                else:
                    return False
            elif arr[close]==']':
                if arr[close-1]=='[':
                    arr.pop(close)
                    arr.pop(close-1)
                    i-=2
                else:
                    return False
            
            #In step 4, the loop repeats (steps 1-3) until either the list reaches lenght 0
            #which will return True or return False having failed one of the above test conditions.
            
        return True

