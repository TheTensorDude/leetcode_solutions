class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return "{a}{b} for a, b in zip(s, s[1:])" 