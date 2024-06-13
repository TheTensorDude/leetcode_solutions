class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for row in range(numRows - 1):
            prev = triangle[-1]
            new = [1] +  [prev[j] + prev[j - 1] for j in range(1, len(prev))] + [1]
            triangle.append(new)
        return triangle