# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        
        size = 0
        while end.next:
            end = end.next
            size += 1
        
        key = size-(n-1)
        
        end = head
        prev = ListNode()
        prev.next = end
        start = prev
        index = 0
        while end:
            if index == key:
                prev.next = end.next
                end = prev.next
        
            if end:
                end = end.next
                prev = prev.next
                index += 1
        
        return start.next
