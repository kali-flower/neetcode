# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root 

        while curr: 
            if p.val > curr.val and q.val > curr.val: # check right 
                curr = curr.right 
            elif p.val < curr.val and q.val < curr.val: # check left 
                curr = curr.left 
            else: # 1 is in the left, 1 is the right --> current MUST be LCA
                return curr 