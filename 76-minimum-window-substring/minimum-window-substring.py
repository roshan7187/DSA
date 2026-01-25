class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = Counter()
        have = 0
        need_count = len(need)

        res = ""
        res_len = float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if c in need and window[c] == need[c]:
                have += 1

            # window is valid
            while have == need_count:
                if (right - left + 1) < res_len:
                    res = s[left:right + 1]
                    res_len = right - left + 1

                # shrink
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return res
