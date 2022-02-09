class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(1,len(nums),2):
            ans += [nums[i]]*nums[i-1]
        return ans
# Runtime: 60 ms, faster than 95.75% of Python3 online submissions for Decompress Run-Length Encoded List.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Decompress Run-Length Encoded List.