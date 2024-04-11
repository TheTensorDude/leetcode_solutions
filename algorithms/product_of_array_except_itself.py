# Time: O(n ^ 2)
# Space: O(1)
# Submission Link: TLE
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        out = []
        for i in range(0, size):
            currentProduct = 1
            for j in range(0, i):
                currentProduct *= nums[j]

            for j in range(i + 1, size):
                currentProduct *= nums[j]
            out.append(currentProduct)
        return out

# --------------- More Optimised ----------------
# Time: O(n)
# Space: O(n)
# Submission Link: https://leetcode.com/problems/product-of-array-except-self/submissions/1229233197
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for num in nums[1:]:
            pre = prefix[-1] * num
            prefix.append(pre)

        size = len(nums)
        postfix = [0] * (size - 1) + [nums[-1]]
        for i in range(size - 2, -1, -1):
            post = nums[i] * postfix[i + 1]
            postfix[i] = post

        prefix.insert(0, 1)
        postfix.append(1)

        output = []
        for index in range(size):
            # Get the answer at "index", we need prefix at 'index - 1'
            # and postfix at 'index + 1'
            currentProduct = prefix[index] * postfix[index + 1]
            output.append(currentProduct)
        return output