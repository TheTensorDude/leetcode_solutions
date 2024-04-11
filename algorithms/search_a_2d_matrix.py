# Time: O(log (mn))
# Space: O(1)
# Submission Link: https://leetcode.com/problems/search-a-2d-matrix/submissions/1229250437?envType=study-plan-v2&envId=top-interview-150
# Trick: Imagine the matrix is flattened, then you can compute the low and high
# and then mid. In which row the mid fall into? mid // n_cols, in which column
# the mid fall into mid % n_cols
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows, n_cols = len(matrix), len(matrix[0])
        size = n_rows * n_cols
        left, right = 0, size - 1
        while left <= right:
            mid = (left + right) // 2
            # Trick
            midElement = matrix[mid // n_cols][mid % n_cols]
            if midElement > target:
                right -= 1
            elif midElement < target:
                left += 1
            else:
                return True
        return False
        