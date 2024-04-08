# Time:  O(n)
# Space: O(n)
# Submission Link: https://leetcode.com/problems/valid-parentheses/submissions/1226491480?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isValid(self, s: str) -> bool:
        cache = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for char in s:
            if char in cache.keys() and stack:
                if cache[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack