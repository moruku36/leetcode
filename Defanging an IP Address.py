"""
Input: address = "1.1.1.1" Output: "1[.]1[.]1[.]1"

Input: address = "255.100.50.0" Output: "255[.]100[.]50[.]0"

与えられたIPアドレスの.を[.]に代えるだけです。
"""
class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace('.','[.]')
        return address
# Runtime: 24 ms, faster than 88.37% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.