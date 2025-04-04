# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return list1
        ans = ListNode()
        ret = ans
        while list1 and list2:
            if list1.val < list2.val:
                ret.val = list1.val
                list1 = list1.next
            else:
                ret.val = list2.val
                list2 = list2.next
            ret.next = ListNode()
            ret = ret.next
        if list1:
            ret.val = list1.val
            ret.next = list1.next
        else:
            ret.val = list2.val
            ret.next = list2.next
        return ans