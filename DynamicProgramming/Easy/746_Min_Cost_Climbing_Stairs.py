"""
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
    Once you pay the cost, you can either climb one or two steps.
    Return the minimum cost to reach the top of the floor.

    cost = [10,15,20]
    Time O(n)
    Space O(n)    
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # from index=0 cost => 10+15
        # from index=1 cost => 15
        min_cost = [0] * len(cost)
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]

        for i in range(2, len(cost)):
            min_cost[i] = cost[i] + min(min_cost[i - 1], min_cost[i - 2])

        return min(min_cost[-1], min_cost[-2])
