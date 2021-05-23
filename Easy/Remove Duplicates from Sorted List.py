# -*- coding: utf-8 -*-
"""
Created on Sun May 23 13:15:10 2021

@author: James Hiu
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        #Set our pointer to the header of the linked list
        p=head
        
        #We need to check every link (pair) in the linked list
        while p is not None and p.next is not None:
                #if the value of the pointer's position and the value of the pointer's next position
                #are equal
                if p.val==p.next.val:
                    #We move the position of pointer #2 two positions away (next.next) as oppose to
                    #one position away.
                    p.next=p.next.next
                else:
                    #Otherwise, the values of the two pointers are different
                    #We advance pointer #1 and continue to check our linked list
                    p=p.next
        
        #return the head once the linked list has been repointed with the logic above.
        return head

