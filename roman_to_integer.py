"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""


class Solution:
    def get_value(self, symbol):
        if symbol == "I":
            return 1
        if symbol == "V":
            return 5
        if symbol == "X":
            return 10
        if symbol == "L":
            return 50
        if symbol == "C":
            return 100
        if symbol == "D":
            return 500
        if symbol == "M":
            return 1000

    def romanToInt(self, s: str) -> int:
        i = 0
        total = 0
        while i < len(s):
            a = self.get_value(s[i])
            if i + 1 > len(s) - 1:
                total += a
                i += 1
            else:
                b = self.get_value(s[i + 1])
                if a < b:
                    total += b - a
                    i += 2
                if a > b:
                    total += a
                    i += 1
                if a == b:
                    total += a
                    i += 1
        return total


print(Solution().romanToInt("III"))
