from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 1st try
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # assumming it is 1->n ordered
        count = 0
        hold = {}
        temp = head

        while temp:
            hold[count] = temp
            count += 1
            temp = temp.next

        idx = (count // 2) + 1
        return hold[idx - 1]

    # Better
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer = head
        fast_pointer = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer
