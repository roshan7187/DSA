class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left =  0
        seen = set()
        summ,maxsum = 0,0

        for right in range(len(nums)):
            while nums[right] in seen:
                summ-=nums[left]
                seen.remove(nums[left])
                left+=1
            
            seen.add(nums[right])
            summ+=nums[right]
            if right - left+1 == k:
                maxsum = max(summ,maxsum)
                seen.remove(nums[left])
                summ-=nums[left]
                left+=1
        return maxsum
        
            