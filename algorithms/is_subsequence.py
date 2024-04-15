# Submission Link: https://leetcode.com/problems/is-subsequence/submissions/1232857462?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Treat it as a stack
        if not s:
            return True
        stack = [c for c in s]
        # Try from behind
        for char in t[::-1]:
            if stack and char == stack[-1]:
                stack.pop()
        return not stack
