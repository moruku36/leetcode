'''
まず、isPalindromeという関数を定義しています。この関数は、文字列sが回文（前から読んでも後ろから読んでも同じになる文字列）であるかどうかを判定するものです。文字列sとその逆順にした文字列s[::-1]が等しいかどうかを返します。

次に、resultという空の文字列を初期化しています。これは最終的に返す最長の回文部分文字列を格納する変数です。

そして、sのすべての可能な部分文字列についてループを行っています。iは0からlen(s)-1まで、jはi+1からlen(s)まで変化させます。このとき、s[i:j]はsのi番目からj-1番目までの部分文字列になります。

それぞれの部分文字列に対して、isPalindrome関数を使って回文であるかどうかをチェックします。もし回文であり、かつresultよりも長い場合は、resultを更新します。

ループが終わったら、resultを返します。
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # helper function to check if a string is a palindrome
        def isPalindrome(s):
            return s == s[::-1]

        # initialize result as empty string
        result = ""

        # loop over all possible substrings of s
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                # get the substring from i to j
                sub = s[i:j]
                # check if it is longer than result and a palindrome
                if len(sub) > len(result) and isPalindrome(sub):
                    # update result
                    result = sub

        # return result
        return result