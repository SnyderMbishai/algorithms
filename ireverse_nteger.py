class Solution:
    def reverse(self, x: int) -> int:
        state = 1
        if x < 0:
            state = -1
        reversed_x = int(str(abs(x))[::-1])
        if reversed_x < -(2**31) or reversed_x > (2**31 - 1):
            return 0
        return reversed_x * state
