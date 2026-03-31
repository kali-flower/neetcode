# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head) # want to init at beginning so it points to head
        left = dummy 
        right = head 

        while n > 0 and right: 
            right = right.next 
            n -= 1

        while right: # keep going until right reaches end of list 
            left = left.next 
            right = right.next 

        left.next = left.next.next # deletes the node by skipping over it 

        return dummy.next
