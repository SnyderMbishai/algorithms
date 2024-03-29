"""
Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it. She decides to share a contiguous segment of the bar selected such that the length of the segment matches Ron's birth month and the sum of the integers on the squares is equal to his birth day. You must determine how many ways she can divide the chocolate.

Consider the chocolate bar as an array of squares, . She wants to find segments summing to Ron's birth day,  with a length equalling his birth month, . In this case, there are two segments meeting her criteria:  and .

Function Description

Complete the birthday function in the editor below. It should return an integer denoting the number of ways Lily can divide the chocolate bar.

birthday has the following parameter(s):

s: an array of integers, the numbers on each of the squares of chocolate
d: an integer, Ron's birth day
m: an integer, Ron's birth month
Input Format

The first line contains an integer , the number of squares in the chocolate bar.
The second line contains  space-separated integers , the numbers on the chocolate squares where .
The third line contains two space-separated integers,  and , Ron's birth day and his birth month.

Constraints

, where ()
Output Format

Print an integer denoting the total number of ways that Lily can portion her chocolate bar to share with Ron.
"""


def birthday(s, d, m):
    no_of_ways = 0
    for i in range(len(s)):
        count = 0
        current_sum = 0
        while count < m and (i + count < len(s)):
            current_sum += s[i + count]
            count += 1

        if current_sum == d:
            no_of_ways += 1

    return no_of_ways


burthdays([1, 2, 1, 3, 2], 3, 2)
