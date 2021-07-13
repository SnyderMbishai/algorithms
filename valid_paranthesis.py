"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:        
    def isValid(self, s):
        v = []
        k_v = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in k_v.values():
                v.append(c)
            elif c in k_v.keys():
                if v == [] or k_v[c] != v.pop():
                    return False
            else:
                return False
        return v == []

    # not good -> takes more time and worse complexity
    def isValid2(self,s):
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()','').replace('{}','').replace('[]','')
        return s == ''


if __name__=='__main__':
    samples = ["()", "()[]{}", "(]",  "([)]", "{[]}"]
    # T, T, F, F, T
    for i in samples:
        print(Solution().isValid(i))
        print(Solution().isValid2(i))