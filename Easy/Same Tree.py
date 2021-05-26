# -*- coding: utf-8 -*-
"""
Created on Tue May 25 20:09:56 2021

@author: James Hiu
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #we want to check to this node where p and q are both empty
        if p == None and q == None:
            #p and q are equal
            return True
        #If p and q are not empty we have to check the node values and traverse the binary tree
        elif p and q:
            #checking if the values are equal
            if p.val == q.val:
                #if they are use recursion to check the nodes on the left and right
                #same strategy as question #94
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

