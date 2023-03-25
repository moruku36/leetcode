class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        first = strs[0]
        last = strs[-1]
        for i in range(len(first)):
            if last[i] != first[i]:
                return first[:i]
        return first
    
s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))

## 文字列の配列から最長の共通接頭辞文字列を見つけるPython関数です。