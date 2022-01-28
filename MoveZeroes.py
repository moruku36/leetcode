"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 1:
            return
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0