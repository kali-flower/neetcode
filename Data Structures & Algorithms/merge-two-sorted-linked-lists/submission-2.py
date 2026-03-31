# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
curr1, curr2 = list1, list2 -> track current values 
if curr 1 <= curr 2 --> append curr2 node to curr1 
curr1.next = curr2?
incremenet pointer at curr2 
else: do the opposite 
create dummy node 
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2: 
            if list1.val < list2.val: 
                node.next = list1
                list1 = list1.next 
            else: 
                node.next = list2 
                list2 = list2.next 

            node = node.next 

        if list1: 
            node.next = list1 
        elif list2: 
            node.next = list2 

        return dummy.next