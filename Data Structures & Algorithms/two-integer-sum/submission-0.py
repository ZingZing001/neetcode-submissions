class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap approach where we will need to recoed each item we have seen and its index position. By calculting the differnece from the current number and the target, and check between the sum of the currrent number and the past numebr. if not seen before add to our list of seen

        seenMap = {}

        for i in range(len(nums)):
            current = nums[i]
            rem = target - current
            if rem in seenMap:
                first = seenMap[rem]
                second = i
                return [first, second]
            seenMap[current] = i






    
            

        