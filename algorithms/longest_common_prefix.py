# Submission Link: https://leetcode.com/problems/longest-common-prefix/submissions/1228477566?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minString = sorted(strs, key = lambda x: len(x))[0]
        for i, char in enumerate(minString):
            if not all([s[i] == char for s in strs]):
                return minString[:i]
        return minString