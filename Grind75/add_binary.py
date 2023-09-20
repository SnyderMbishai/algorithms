"""
67. Add Binary - https://leetcode.com/problems/add-binary/description/
Easy

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        reversed_a = a[::-1]
        reversed_b = b[::-1]

        result = ""

        carry = 0

        for i in range(max(len(a), len(b))):
            first_digit = int(reversed_a[i]) if i < len(a) else 0
            second_digit = int(reversed_b[i]) if i < len(b) else 0

            total = first_digit + second_digit + carry

            mini_total = total % 2
            result = str(mini_total) + result

            new_carry = total // 2
            carry = new_carry

        if carry:
            return str(carry) + result

        return result
