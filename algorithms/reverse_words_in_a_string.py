# Time: O(n)
# Space: O(k), k = #words
# Submission Link: https://leetcode.com/problems/reverse-words-in-a-string/submissions/1226608236?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        length = len(s)
        # End is exclusive
        start, end = length - 1, length
        out = []
        while start > 0:
            start -= 1
            if s[start] == ' ':
                out.append(s[start + 1: end])
                # Go back as long as we encounter space
                while s[start] == ' ':
                    start -= 1
                # End if exclusive
                end = start + 1
        # Append the first chunk
        out.append(s[start : end])
        return ' '.join(out)