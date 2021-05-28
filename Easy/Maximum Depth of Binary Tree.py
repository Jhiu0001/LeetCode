# -*- coding: utf-8 -*-
"""
Created on Thu May 27 23:27:27 2021

@author: James Hiu
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Determine the max depth of the tree
        # if there is no root node ,then return zero
        if(root is None):
            return 0
        
        #Next we use recursion to call the function adding one for every level we go deep into the tree
        #because the tree can take on various shape on the path down... we take the max
        #+1 because we count the root node
        #if a tree is only the root node then the max depth to the left and right would return (0,0)
        return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))

