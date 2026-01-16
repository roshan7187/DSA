class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        index = 0
        ans = []
        n = len(nums)
        nums.sort()
        while index < n - 2 :

            left,right = index+1, n-1
            
            if index > 0 and nums[index] == nums[index-1] :
                index+=1
                continue

            while left < right :
                if nums[index] + nums[left] + nums[right] == 0 :
                    triplet = [nums[index] , nums[left] , nums[right]]
                    ans.append(triplet)
                    left+=1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    

                elif nums[index] + nums[left] + nums[right] > 0 :
                    right-=1
                else :
                    left+=1
            index+=1
        return ans