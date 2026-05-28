class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = {}
        for index, val in enumerate(s):
            hash_map[val] = hash_map.get(val, 0) + 1

        for index, val in enumerate(t):
            if val not in hash_map.keys():
                return False
            hash_map[val] = hash_map.get(val) - 1

        if list(hash_map.values()) == [0 for i in range(len(set(s)))]:
            return True
        else:
            return False