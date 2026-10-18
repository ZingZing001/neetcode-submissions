import itertools
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        inverted_dict = {}
        result = []
        output = []
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] = freqMap[num] + 1
        results = list(freqMap.items())
        results = sorted(results, key=lambda x: x[1])
        for i in range(k):
            pair = results.pop()
            result = pair[0]
            output.append(result)
        return output