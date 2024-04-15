# Submission Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/1232851986?envType=study-plan-v2&envId=top-interview-150https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/1232851986?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        windowSize = len(needle)
        arrSize = len(haystack)
        for i in range(arrSize - windowSize + 1):
            window = haystack[i : i + windowSize]
            if window == needle:
                return i
        return -1