class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        result = 0

        while x > 0:
            rem = x % 10
            result = (result * 10) + rem
            x //= 10
        return result == num