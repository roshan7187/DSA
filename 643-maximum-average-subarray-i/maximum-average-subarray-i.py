class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        summ = sum(nums[:k])
        maxavg = summ/k
        left = 0
        for right in range(k,len(nums)) :
            summ+=nums[right]
            summ-=nums[left]
            left+=1

            maxavg = max(maxavg,summ/k)
                
        return maxavg