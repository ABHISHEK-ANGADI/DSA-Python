class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        n = len(s)

        j = -1
        while j >= (-1*n) and s[j] != " ":
            j -= 1

        j += 1
        j *= -1

        return j
        