class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hsNums = set(sorted(nums))
        counter = 0
        longest = 0
        for num in hsNums:
            if num - 1 not in hsNums:
                counter += 1
                while num + counter in hsNums:
                    counter += 1
                if counter > longest:
                    longest = counter
            counter = 0
        return longest
                

        


        
            


            
            


        

        