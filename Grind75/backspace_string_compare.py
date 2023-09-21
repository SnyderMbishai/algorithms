""" 

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?

"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # preferred
        def process_using_list(st):
            st_ = []
            for i in st:
                if i == "#":
                    if st_:
                        st_.pop()
                else:
                    st_.append(i)

        # first attempt
        def process_string(st):
            st_ = ""
            for i in range(len(st)):
                if st[i] != "#":
                    st_ = st_ + st[i]
                else:
                    if i > 0:
                        st_ = st_[:-1]
            return st_

        return process_using_list(s) == process_using_list(t)
