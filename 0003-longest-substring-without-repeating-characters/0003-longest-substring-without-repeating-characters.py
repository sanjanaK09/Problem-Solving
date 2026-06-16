class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_index = {}
        max_length = 0
        left = 0
        for right, char in enumerate(s):
            if char in char_to_index and char_to_index[char] >= left:
                left = char_to_index[char] + 1
            char_to_index[char] = right
            max_length = max(max_length, right - left + 1)
        return max_length
       