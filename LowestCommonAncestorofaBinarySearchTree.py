## Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

## According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

## Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
## Output: 6
## Explanation: The LCA of nodes 2 and 8 is 6.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left != None and right != None:
            return root
        
        if left == None:
            return right
        if right == None:
            return left
          
## lessons learnt:
## base case1: if there is no root node.
## base case2: if p or q are equal to root then return root
## average case1: if left != none and right != none then return root
## average case2: if left == none then return right
## average case3: if right == none then return left
