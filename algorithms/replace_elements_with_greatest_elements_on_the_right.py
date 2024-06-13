class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        out = [-1] * size
        print(out)
        for i in range(size - 1, 0, -1):
            out[i - 1] = max(out[i], arr[i])
        return out
