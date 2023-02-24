class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -=1
            steps += 1
        return steps
# Runtime: 28 ms, faster than 68.90% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.