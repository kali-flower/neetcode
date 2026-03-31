# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_val): 
            if not node: 
                return 0 

            if node.val >= max_val: 
                result = 1 
            else: 
                result = 0 
            max_val = max(max_val, node.val)

            # these function just count the number of good nodes 
            # for each node, we first update the max values 
            result += dfs(node.left, max_val) 
            result += dfs(node.right, max_val)
            
            return result
        return dfs(root, root.val)
