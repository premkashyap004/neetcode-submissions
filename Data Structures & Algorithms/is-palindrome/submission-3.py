class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined = []
        for char in s:
            if char.isalnum():
                refined.append(char.lower())
        refined_str = "".join(refined)
        return refined_str == refined_str[::-1]