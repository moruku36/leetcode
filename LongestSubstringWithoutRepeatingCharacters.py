"""
Given a string s, find the length of the longest substring without repeating characters.


"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp = {}
        start = res = 0
        for i, c in enumerate(s):
            if c in tmp and start <= tmp[c]:
                start = tmp[c] + 1
            else:
                res = max(res, i - start + 1)
            tmp[c] = i
        return res