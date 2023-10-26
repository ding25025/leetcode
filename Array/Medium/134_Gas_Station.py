"""
    Given two integer arrays gas and cost, 
    return the starting gas station's index if you can travel around the circuit once in the clockwise direction, 
    otherwise return -1. If there exists a solution, it is guaranteed to be unique
    Time - O(n)
    Space - O(1)
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        idx = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                idx = i + 1
        return idx
