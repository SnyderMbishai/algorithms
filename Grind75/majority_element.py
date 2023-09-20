from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        checked = []
        most = 0
        char = 0
        for num in nums:
            if num not in checked:
                num_count = nums.count(num)
                if num_count > most:
                    most = num_count
                    char = num
                checked.append(num)
        return char
