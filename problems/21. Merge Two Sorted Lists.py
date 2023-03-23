from typing import Optional


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = result = ListNode()
        while list1 or list2:
            if list1.val < list2.val:
                cur.next = list1
                cur, list1 = list1, list1.next
            else:
                cur.next = list2
                cur, list2 = list2, list2.next
        if list1 or list2:
            cur.next = list1 or list2
        return result.next
