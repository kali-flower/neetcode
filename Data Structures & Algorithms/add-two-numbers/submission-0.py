# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        curr = dummy 

        carry = 0 
        while l1 or l2 or carry: # edge case of carry existing --> 9 + 9 = 18
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 

            # find new digits 
            val = val1 + val2 + carry 
            carry = val // 10 # if we have 19, 19//10 = 1 (integer div)
            val = val % 10 # only the 9 goes into the list 

            curr.next = ListNode(val) 

            # update pointers 
            l1 = l1.next if l1 else None  
            l2 = l2.next if l2 else None # if there is no next val 
            curr = curr.next 

        return dummy.next 