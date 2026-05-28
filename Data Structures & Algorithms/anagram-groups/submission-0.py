class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_strs = {}

        for word in strs:
            hash_map = [0 for i in range(26)]

            for char in word:
                order = ord(char) - ord('a')
                hash_map[order] +=1
            
            key = str(hash_map)
            if not grouped_strs.get(key): 
                grouped_strs[key] = []
            grouped_strs[key].append(word)
        return [val for val in grouped_strs.values()]