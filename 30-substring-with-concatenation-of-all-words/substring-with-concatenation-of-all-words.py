from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        word_len = len(words[0])
        num_words = len(words)
        
        target = {}
        for w in words:
            if w in target:
                target[w] += 1
            else:
                target[w] = 1

        ans = []

        for offset in range(word_len):
            left = offset
            seen = {}
            count = 0

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in target:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    while seen[word] > target[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == num_words:
                        ans.append(left)

                else:
                    seen = {}
                    count = 0
                    left = right + word_len

        return ans