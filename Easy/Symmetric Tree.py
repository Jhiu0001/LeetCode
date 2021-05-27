# -*- coding: utf-8 -*-
"""
Created on Wed May 26 23:01:39 2021

@author: James Hiu
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #We want to check if the binary tree is a mirror image of itself
        #first we check the special case if the tree is empty
        if root==None:
            #if the tree is empty, return true
            return True
        else:
            #otherwise we need to move to the left and right nodes of the tree
            #we are also building a second definition, Reflect to check the mirror image
            return self.Reflect(root.left, root.right)

    def Reflect(self, left, right):
        #if we have reached the end of the tree and the left and right nodes of the binary tree path is empty
        if left is None and right is None:
            #return true because we will have checked everything at this point
            return True
        #Another scenario is that one node will exist but its mirror image will not
        if left is None or right is None:
            #we can stop the process, return flase and say the tree is not symmetric
            return False

        #The most common scenario traversing the tree is that we will have to compare the left and right values
        #if the values are equal we will have to go a level deeper into the tree comparing more nodes
        #2^(n-1), comparsions for every level we move down into the tree, root node, n=0
        if left.val == right.val:
            #we need to check the outer nodes, left-left node with right-right node
            out= self.Reflect(left.left, right.right)
            #we also need to check inner nodes, left-right node with right-left node
            #these patterns will be called in a recursion
            inner= self.Reflect(left.right, right.left)
            return out and inner
        else:
            #if the mirrior image values are unequal we can return false
            return False

