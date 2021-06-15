class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_t = x
        original = 0
        while original > 0:
            last = original%10
            print(last,'===0')
            reversed_t = reversed_t*10 + last
            original = original//10
            print(original)
        print(reversed_t, x)
        return x == reversed_t
    
    def isPalindrome2(self, x: int) -> bool:
        """ Convert the integer to a string first """
        return str(x) == str(x)[::-1]

if __name__=='__main__':
    Solution().isPalindrome(x = 10)
    Solution().isPalindrome(10)