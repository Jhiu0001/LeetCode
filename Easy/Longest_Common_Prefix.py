# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:56:03 2021

@author: James Hiu
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """      
        
        #Initiate an empty string
        longest_prefix=''
        
        #The shortest word in the list is the upper bound of the lengthiest possible prefix
        shortest_word=min(len(x) for x in strs)
        
        #Initiate the a counter i counting up to the length of the shortest word
        i=0
        
        #In our while loop we going to check if each letter in the list at position "i" is the same
        while i < shortest_word:
            #A loop within a loop, to interate through each word
            #Iniaite / Reset "j" to 0, the first word in the word list
            j=0
            
            while j <len(strs)-1:
                #Check if all words have the same i-th letter
                if strs[j][i]==strs[j+1][i]:
                    j+=1
                    continue
                else:
                    #As soon as we have unmatched i-th letters, return the answer up to that point 
                    return longest_prefix
                
            #If all words have the same i-th letter, add the letter to the longest_prefix variable
            longest_prefix+=strs[0][i]
            
            #Move onto the next letter
            i+=1     
        
        #the outer while loop fully runs, the shortest word is also the longest prefix, return the answer
        #ie. [self, selfish, self defense] -->'self'
        return longest_prefix  

