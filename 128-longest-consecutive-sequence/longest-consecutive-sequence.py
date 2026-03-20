class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:   
                curr = num
                streak = 0

                while curr in num_set:
                    curr += 1
                    streak += 1

                longest = max(longest, streak)

        return longest 