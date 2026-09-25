from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The common pattern will be that they will have the same letter if they are sorted
        initDict = defaultdict(list)
        # print(initDict)
        for word in strs:
            key = "".join(sorted(word))
            initDict[key].append(word)
        return list(initDict.values())