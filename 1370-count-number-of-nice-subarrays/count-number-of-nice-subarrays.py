class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = 0
        ans = 0
        freq = {0: 1}

        for num in nums:
            if num % 2 == 1:
                prefix += 1

            if prefix - k in freq:
                ans += freq[prefix - k]

            freq[prefix] = freq.get(prefix, 0) + 1

        return ans