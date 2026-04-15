class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix_sums = [1] * n
        suffix_sums = [1] * n
        result = [0] * n
   
      

        for i in range(1,n):
            prefix_sums[i] = nums[i-1] * prefix_sums[i-1]

        for j in range(n-2,-1,-1):
            suffix_sums[j] = nums[j+1] *suffix_sums[j+1]

        for k in range(n):
            result[k] = prefix_sums[k] * suffix_sums[k]


        return result 

