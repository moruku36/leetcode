class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return target

# Runtime: 36 ms, faster than 36.25% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Create Target Array in the Given Order.