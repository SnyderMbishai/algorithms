class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseLinkedList(self, head: ListNode) -> Optional([ListNode]):
        prev = None
        curr = head

        while curr:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr

        return prev
