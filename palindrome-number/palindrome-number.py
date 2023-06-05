class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        # reverse the integer
        reversed_num = 0
        temp = x
        while temp > 0:
            reversed_num = (reversed_num * 10) + (temp % 10)
            temp //= 10

        # check if the reversed integer is equal to the original integer
        return reversed_num == x