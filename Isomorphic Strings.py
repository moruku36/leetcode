class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Initialize an empty dictionary
        mapping = {}
        # Loop through each pair of characters in s and t
        for c1, c2 in zip(s, t):
            # Check if c1 is already mapped to c2
            if c1 in mapping:
                # If yes, verify that the mapping is consistent
                if mapping[c1] != c2:
                    # If not, return False
                    return False
            else:
                # Check if c2 is already mapped to another character
                if c2 in mapping.values():
                    # If yes, return False
                    return False
                else:
                    # If not, add the mapping to the dictionary
                    mapping[c1] = c2
        # Return True at the end
        return True