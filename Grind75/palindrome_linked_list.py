"""

234. Palindrome Linked List
Solved
Easy
Topics
Companies
Given the head of a singly linked list, return true if it is a palindrome
 or false otherwise.

 

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9
"""



from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # first try
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals == vals[::-1]

    # optimized
