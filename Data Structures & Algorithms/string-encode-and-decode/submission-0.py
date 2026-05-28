class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        
        return result

    def decode(self, s: str) -> List[str]:
        words = []
        pointer = 0
        i = 0
        while i<len(s): 
            if s[i] == "#":
                count = int(s[pointer:i])
                pointer = i + count + 1
                words.append(s[i+1:pointer])
                i=pointer
            else:
                i+=1
        return words

