# Time: O(n^3)
# Space: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        out = 0
        size = len(s)
        for i in range(size - 1):
            for j in range(i, size):
                chunk = s[i : j + 1]
                if len(set(chunk)) == len(chunk):
                    out = max(len(chunk), out)
        return out