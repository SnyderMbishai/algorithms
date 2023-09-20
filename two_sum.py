"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


# def twoSum(nums, target:
#     for idx, value in enumerate(nums):
#         diff = target - value
#         if diff in nums and nums.index(diff) != idx:
#             return idx, nums.index(diff)


def twoSumNoRepeats(nums, target):
    for idx, number in enumerate(nums):
        other_number = target - number
        if other_number in nums[idx + 1 :]:
            return idx, nums[idx + 1 :].index(other_number) + idx + 1


if __name__ == "__main__":
    arr = [5, 3, 5]
    target = 10
    print(twoSumNoRepeats(arr, target))
