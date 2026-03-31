# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
    head -> a -> b -> c -> d -> none 
 ^    ^                           ^     ^ 

 head = start of linked list, points to next node 
curr = head 
prev = None 

temp = curr.next -> save value
curr.next = prev -> point her backwards
prev = curr -> shift prev forward 
curr = temp -> shift curr to next node 

stop when we reach the last thing (none)
'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr, prev = head, None

        while curr: 
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 

        return prev 
