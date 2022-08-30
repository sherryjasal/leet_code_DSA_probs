## Given the roots of two binary trees p and q, write a function to check if they are the same or not.

## Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



## Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and
               self.isSameTree(p.right, q.right))
      
      
## lessons learnt
## base case1: when both the trees have null node, return True
## base case2: when either of the roots are null, return False
## base case3: when both of them have different values in root node, return False
## combine case 2 and 3
## otherwise return self.isSameTree(left sides of p and q) and self.isSameTree(right sides of p and q)
        
