# Time:  O(n)
# Space: O(1)
# Submission Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1226476271?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniques = set()
        k = 0
        for num in nums:
            if num not in uniques:
                uniques.add(num)
                nums[k] = num
                k += 1
        return k