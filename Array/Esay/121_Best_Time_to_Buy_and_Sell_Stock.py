"""
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    Time: O(n)
    Space: O(1)
    Tip: Sliding Window
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # default set first day
        buy = prices[0]
        profit = 0

        for sell in range(1, len(prices)):
            if prices[sell] > buy:
                profit = max(profit, prices[sell] - buy)
            else:
                buy = prices[sell]
        return profit
