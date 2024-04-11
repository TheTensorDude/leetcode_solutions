# Time: O(n)
# Space: O(1)
# Implements voting algorithm, think about KNN
# Submission Link: 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_elem, count = nums[0], 1
        for num in nums[1:]:
            if num == majority_elem:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majority_elem = num
                    count = 1
        return majority_elem