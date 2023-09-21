"""

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


Example 1:

Input: n = 2
Output: [0,1,1]

Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]

Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:

0 <= n <= 10^5

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

"""

from typing import List


class Solution:
    # take 1
    def countBits(self, n: int) -> List[int]:
        current_binary = 0
        ans = [0]

        def add_binary(a, b):
            res = ""
            carry = 0
            str_a_reversed = str(a)[::-1]
            str_b_reversed = str(b)[::-1]
            for i in range(max(len(str_a_reversed), len(str_b_reversed))):
                first = int(str_a_reversed[i]) if i < len(str_a_reversed) else 0
                second = int(str_b_reversed[i]) if i < len(str_b_reversed) else 0

                sm = first + second + carry
                carry_ = sm // 2
                res_ = sm % 2

                res = str(res_) + res
                carry = carry_

            return str(carry) + res if carry else res

        for i in range(n):
            next_binary = add_binary(current_binary, 1)
            ans.append(next_binary.count("1"))
            current_binary = next_binary

        return ans

    # Dynamic Programming -> Recomended
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i

            dp[i] = 1 + dp[i - offset]

        return dp
