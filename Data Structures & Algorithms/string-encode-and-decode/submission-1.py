class Solution:
    def encode(self, strs: List[str]) -> str:
        parts = []
        for word in strs:
            parts.append(str(len(word)) + "#" + word)
        return "".join(parts)

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

