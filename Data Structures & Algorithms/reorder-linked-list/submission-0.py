# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
can build an extra array, put the nodes in the array, and then reform 
back into a linked list
'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = [] 
        curr = head 
        while curr: 
            nodes.append(curr)
            curr = curr.next 

        left, right = 0, len(nodes) - 1
        while left < right: 
            nodes[left].next = nodes[right] # 1st value will point to second value
            left += 1 

            nodes[right].next = nodes[left]
            right -= 1

        nodes[left].next = None