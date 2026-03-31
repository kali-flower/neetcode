# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        fast and slow pointer 
        slow pointer goes node.next 
        fast goes node.next.next 
        if they ever cross, that means that there is a cycle somewhere 
        '''
        slow, fast = head, head 

        while fast and fast.next: # while fast to make sure the list isnt empty
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast: 
                return True 

        return False 
