# Time: O(n)
# Space: o(1)
# Submission Link: https://leetcode.com/problems/remove-element/submissions/1226047244?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k, length = 0, len(nums)
        for num in nums:
            if num != val:
                nums[k] = num 
                k += 1
        return k