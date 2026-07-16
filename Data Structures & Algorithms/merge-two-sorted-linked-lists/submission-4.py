# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = None
        first = ListNode()

        while list1 or list2:
            if (list1 == None):
                if (curr == None):
                    return list2   
                else:   
                    curr.next = list2     
                    return first.next
            elif (list2 == None):
                if (curr == None):
                    return list1
                else:
                    curr.next = list1
                    return first.next
            else:
                if (list1.val >= list2.val):
                    if (curr == None):
                        curr = list2
                        first.next = curr
                        list2 = list2.next
                    else:
                        curr.next = list2
                        curr = curr.next
                        list2 = list2.next
                else:
                    if (curr == None):
                        curr = list1
                        first.next = curr
                        list1 = list1.next
                    else:
                        curr.next = list1
                        curr = curr.next
                        list1 = list1.next
            