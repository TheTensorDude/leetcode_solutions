# Time: O(n)
# Space: O(1)
# Submission Link: https://leetcode.com/problems/longest-consecutive-sequence/submissions/1195689406
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        count = 0
        for num in uniqueNums:
            if num - 1 not in uniqueNums:
                currentCount = 0
                while num in uniqueNums:
                    num += 1
                    currentCount += 1
                count = max(currentCount, count)
                print(count)

        return count