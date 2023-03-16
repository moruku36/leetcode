class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize an empty set and two pointers
        seen = set()
        i = 0
        j = 0
        answer = 0
        
        # Loop over the string with j as index
        while j < len(s):
            # If s[j] is not in seen, add it and update answer
            if s[j] not in seen:
                seen.add(s[j])
                answer = max(answer, j - i + 1)
                j += 1
            # If s[j] is in seen, remove s[i] and increment i
            else:
                seen.remove(s[i])
                i += 1
        
        # Return answer at end
        return answer
