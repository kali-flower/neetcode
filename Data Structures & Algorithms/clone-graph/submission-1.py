"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
map old nodes to new nodes using hashmap 
oldnode: newnode
'''

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {}

        def dfs(node): 
            if node in mapping: # already made clone 
                return mapping[node]

            copy = Node(node.val)
            mapping[node] = copy 

            for item in node.neighbors:     
                copy.neighbors.append(dfs(item))

            return copy 

        if node: 
            return dfs(node)
        else: 
            return None