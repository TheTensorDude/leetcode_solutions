# Time: O(n)
# Space: O(1)
# Submission Link: https://leetcode.com/problems/length-of-last-word/submissions/1228471112?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        size = len(s) - 1
        while size >= 0 and s[size] != ' ':
            size -= 1
        return len(s) - size - 1