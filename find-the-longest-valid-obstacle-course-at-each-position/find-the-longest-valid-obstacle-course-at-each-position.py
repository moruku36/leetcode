from typing import List
import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dp = []
        res = []
        for a in obstacles:
            i = bisect.bisect_right(dp, a)
            if i == len(dp):
                dp.append(a)
            else:
                dp[i] = a
            res.append(i + 1)
        return res
