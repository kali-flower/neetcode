# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = [] 
        q = deque([root])

        while q: 
            right = None # get the rightmost element, initially it's None  
            q_len = len(q) 

            for i in range(q_len): 
                node = q.popleft()
                if node: 
                    right = node # will end up being the LAST one added
                    q.append(node.left)
                    q.append(node.right)

            if right: 
                result.append(right.val)

        return result 