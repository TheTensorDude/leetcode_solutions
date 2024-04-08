# Time: O(n^2) | TLE but good practice to solve both ways
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                currentProfit = prices[j] - prices[i]
                maxProfit = max(maxProfit, currentProfit)
        return maxProfit
    
# ----------------- More optimized ----------------------
# Time: O(n)
# Space: O(1)
# Submission Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1226058782?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = float('inf'), 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            # minPrice = min(price, minPrice)
            currentProfit = price - minPrice
            maxProfit = max(maxProfit, currentProfit)
        return maxProfit