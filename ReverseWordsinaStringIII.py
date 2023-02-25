"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        reversed_words = []
        for word in words:
            reversed_words.append(word[::-1])

        return " ".join(reversed_words)