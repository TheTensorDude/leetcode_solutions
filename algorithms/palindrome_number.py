# Cheating
# Submission Link: https://leetcode.com/problems/palindrome-number/submissions/1229546934?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]