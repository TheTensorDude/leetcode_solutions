# Time: O(n)
# Space: O(1)
# Submission Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1226593813?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def twoSum( self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            currentSum = numbers[left] + numbers[right]
            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                return [left + 1, right + 1]
                
# ---------------- Another Approach -----------------
# Also works for Two Sum
# Time: O(n)
# Space: O(n)
# Submission Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1226596619?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def twoSum( self, numbers: List[int], target: int) -> List[int]:
        cache = dict()
        for index, num in enumerate(numbers):
            complement = target - num 
            if complement in cache.keys():
                return [cache[complement], index + 1]
            cache[num] = index + 1
