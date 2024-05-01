# Time: O(n^3)
# Space: O(n)
# Submission Link: TLE at 986/987
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
    
    
# Sliding Window with Two Pointer
# Time: O(n)
# Space: O(n)
# But this below solution seems slow kinda dude :(
# Submission Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1235174485
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        out = 0
        left, right = 0, 0
        numSet = set()
        while right < size:
            if s[right] not in numSet:
                numSet.add(s[right])
                right += 1
            else:
                numSet.remove(s[left])
                left += 1
            out = max(right - left, out)
        return out