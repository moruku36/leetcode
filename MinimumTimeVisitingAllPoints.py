class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        sec = 0
        x1,y1 = points.pop()
        while points:
            x2,y2 = points.pop()
            sec += max(abs(x2-x1),abs(y2-y1))
            x1,y1 = x2,y2
        return sec
# Runtime: 56 ms, faster than 84.71% of Python3 online submissions for Minimum Time Visiting All Points.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Minimum Time Visiting All Points.