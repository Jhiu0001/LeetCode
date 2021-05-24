# -*- coding: utf-8 -*-
"""
Created on Mon May 24 15:43:38 2021

@author: James Hiu
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        #In order traversal of a binary tree means to process all nodes of a tree by recursively
        #processing the left subtree, then processing the root, and finally the right subtree.
        
        ## example              1
        ##                    /   \
        ##                   2     3
        ##                  / \   / \
        ##                 4   5 6   7
        ## should return [4,2,5,1,6,3,7]
        
        
        #Initialize an empty array
        arr=[]

        #We use recursion to solve this problem         
        if root:
            #We want to first move down the left side of the tree
            arr = self.inorderTraversal(root.left)
            #Next we want to append the value of the node to our list
            arr.append(root.val)
            #Next want to move down the right side of the tree
            arr = arr + self.inorderTraversal(root.right)
        return arr

