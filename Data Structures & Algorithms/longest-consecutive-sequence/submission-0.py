class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numbers = set(nums)
        count = 0

        for i in nums:
            if i - 1 not in numbers:
                length = 0
                while i + length in numbers:
                    length = length + 1 
                
                count = max(count , length)

        return count



        