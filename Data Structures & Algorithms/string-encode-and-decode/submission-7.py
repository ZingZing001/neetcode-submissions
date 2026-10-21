class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 1 and strs[0] == "#":
            clean = "#"
            return clean
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#" + strs[i]
        clean = "".join(strs)
        return clean


    def decode(self, s: str) -> List[str]:
        digit = 0
        pint1 = 0
        word = []
        if not s:
            return []
        if s[0] == "#":
            return ["#"]
        i = 0
        while i < len(s):
            if s[i] == "#":
                digit = int(s[pint1:i])
                word.append(s[i+1:digit+i+1])
                pint1 = digit + i + 1
                i = digit+i+1
            i += 1
        return word


            
        
