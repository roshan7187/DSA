class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [0]*n
        left = 0
        right = n-1
        pos = n-1

        while(left<=right):
            if abs(nums[left]) > abs(nums[right]) :
                res[pos] = nums[left] ** 2
                left+=1
            else:
                res[pos] = nums[right] **2
                right-=1
            pos-=1
        return res
