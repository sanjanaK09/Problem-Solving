class Solution:
    def longestPalindrome(self, s: str) -> str:
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                end = start + length
                substring = s[start:end]
                if substring == substring[::-1]:
                    return substring
        return ""
       