class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n-3):
            for j in range(i+1, n-2):
                d = {}
                for k in range(j+1, n):
                    if target-nums[i]-nums[j]-nums[k] in d:
                        ans.add((nums[i], nums[j], nums[k], nums[d[target-nums[i]-nums[j]-nums[k]]]))
                    d[nums[k]] = k
        return list(ans)