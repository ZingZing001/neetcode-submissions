class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}

        for char in s:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
        
        for char in t:
            if char not in counts:
                return False
            else:
                counts[char] -= 1
        
        for value in counts.values():
            if value != 0:
                return False
        return True
        