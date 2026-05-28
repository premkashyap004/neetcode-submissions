class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined_str = ""
        for char in s:
            if char.isalnum():
                refined_str += char.lower()

        return refined_str == refined_str[::-1]