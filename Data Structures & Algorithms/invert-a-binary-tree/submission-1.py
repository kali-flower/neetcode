# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
check if root exists 
call recursively on left and right subtree 
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None 
        
        root.left, root.right = root.right, root.left 
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 