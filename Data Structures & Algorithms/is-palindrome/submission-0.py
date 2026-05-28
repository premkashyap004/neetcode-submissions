class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined_str = ""
        for char in s:
            if char.isalnum():
                refined_str += char.lower()

        print(refined_str[::-1],refined_str)
        return refined_str == refined_str[::-1]