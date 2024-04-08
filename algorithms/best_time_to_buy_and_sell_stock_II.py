# Time: O(n)
# Space: O(1)
# Submission Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/1226550521?envType=study-plan-v2&envId=top-interview-150

# Trick: We want to count all the profit when the line is going up
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        length = len(prices)
        for i in range(1, length):
            currentProfit = prices[i] - prices[i - 1]
            if currentProfit > 0:
                totalProfit += currentProfit
        return totalProfit