from collections import Counter


class Solution:
    def longestPalindrome_1(self, s: str) -> int:
        count = 0
        checked = []
        b = s
        for i in s:
            if i in checked:
                b = b.replace(i, "", 1)
                checked.remove(i)
                count += 2
            else:
                checked.append(i)
        if len(checked) >= 1:
            count += 1
        return count

    def longestPalindrome_2(self, s: str) -> int:
        chars = []
        for i in s:
            chars.remove(i) if i in chars else chars.append(i)
        return (len(s) - len(chars)) + 1 if len(chars) else len(s)

    # counters
    def longestPalindrome_4(self, s: str) -> int:
        counts = Counter(s)
        longest = 0

        for count in counts.values():
            longest += int(count / 2) * 2
            if not longest % 2 and count % 2:
                longest += 1
        return longest

    # Preffered
    def longestPalindrome_3(self, s: str) -> int:
        chars = set()
        for i in s:
            chars.remove(i) if i in chars else chars.add(i)
        return (len(s) - len(chars)) + 1 if len(chars) else len(s)
