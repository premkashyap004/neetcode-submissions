class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}

        for word in strs:
            bucket = [0] * 26
            
            for char in word:
                bucket[ord(char) - ord('a')] +=1
            
            if not group_anagrams.get(str(bucket)):
                group_anagrams[str(bucket)] = []
            group_anagrams[str(bucket)].append(word)
        
        return [val for _, val in group_anagrams.items()]