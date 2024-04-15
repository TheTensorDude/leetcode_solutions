# Submission Link: https://leetcode.com/problems/valid-palindrome/submissions/1232855118?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # We need to convert all uppercase to lowercase and discard leading and trailing spaces
        s = s.lower().strip()
        size = len(s)
        low = 0
        high = size - 1
        while low < high:
            if not s[low].isalnum():
                low += 1
                continue
            if not s[high].isalnum():
                high -= 1
                continue
            
            if s[low] != s[high]:
                return False
            
            low += 1
            high -= 1
        return True