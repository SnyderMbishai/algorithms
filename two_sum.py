class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            diff = target - value
            if diff in nums and nums.index(diff) != index:
                return index, nums.index(diff)
                
    def twoSumNoRepeats(nums, target)
        for idx,number in enumerate(nums):
            other_number = target - number            
            if other_number in nums[idx+1:]:
                return nums.index(number), nums[idx+1:].index(other_number)+idx+1