class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            diff = target - value
            if diff in nums and nums.index(diff) != index:
                return index, nums.index(diff)
