# -*- coding: utf-8 -*-
"""
Created on Sun May 16 12:33:28 2021

@author: James Hiu
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        #Step 1
        #If one of the linked list is an empty list, simply return the other list
        #Note: if both list are empty lists this soultion would still work
        if not l1:
            return l2
        if not l2:
            return l1
        
        #Step 2
        #We are going to build our own linked list to solution this question 
        #We identify which linked list starts with the smaller number
        #If l1 and l2 are equal, then pick l1 (it will not matter)
        #Whether l1 or l2 is picked we move onto the next item in the linked list, list.next
        if l1.val<=l2.val:
            head=l1
            l1=l1.next 
        else:
            head=l2
            l2=l2.next
               
        #Step 3
        #set our pointer p equal to head
        p=head
                
        #Step 4
        #continue to make l1 vs l2 linked list comparision picking the smaller number
        #we set the next number of our linked list equal to the number identified from l1 or l2
        #we make sure we increment our pointer and the appropriate linked list accordingly
        while l1 and l2:
            if l1.val<=l2.val:
                p.next=l1
                l1=l1.next 
            else:
                p.next=l2
                l2=l2.next
            p=p.next
        
        #Step 5
        #one linked list is likely to report its last number prior to the other, l1 or l2
        #in this scenario, the remainder of our linked list is to simply enumerate the remaining numbers
        #from the remaining list.
        if not l1:
            p.next=l2
        if not l2:
            p.next=l1
        
        return head


