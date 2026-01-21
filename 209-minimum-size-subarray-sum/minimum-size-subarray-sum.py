class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        summ = 0
        minlen = len(nums) +1
        for right in range(len(nums)) :
            summ+=nums[right]

            while summ >= target :
                minlen = min(minlen,right-left+1)
                summ -= nums[left]
                left+=1
        
        if minlen == len(nums)+1 :
            return 0 
        else :
            return minlen