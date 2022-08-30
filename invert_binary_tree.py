## Given the root of a binary tree, invert the tree, and return its root.
## meaning : swapping children

## Input: root = [4,2,7,1,3,6,9]
## Output: [4,7,2,9,6,3,1]

## Input: root = [2,1,3]
## Output: [2,3,1]

## Input: root = []
## Output: []
## base case: if no root, then None
## Swapping case : Using recursion



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ## base case
        if not root:
            return None
        ##sawp children
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
      
      
      
## lessons learnt: 
## check base case if no root is there then None
## otherwise do the swapping
## store it in temp , the left side of the tree
## then left = right
## right will become the temp
## use self.invertTree(root.left)
## self.invertTree(root.right) 
## if we will not do the self it will give us the exact same tree but what we want is children position are also swapped = Left Right = Right Left 
## eg. 69 = 96 
