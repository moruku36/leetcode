class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        def f(c):
            return ord(c) - 97

        ct_s, ct_p = [0] * 26, [0] * 26
        for c in p:
            ct_p[f(c)] += 1
        l = len(p)
        for c in s[: l - 1]:
            ct_s[f(c)] += 1
        for i, c in enumerate(s[l - 1:]):
            ct_s[f(c)] += 1
            if ct_s == ct_p:
                return True
            ct_s[f(s[i])] -= 1
        return False