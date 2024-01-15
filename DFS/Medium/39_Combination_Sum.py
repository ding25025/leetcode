"""
    Given an array of distinct integers candidates and a target integer target, 
    return a list of all unique combinations of candidates where the chosen numbers sum to target. 
    You may return the combinations in any order.
    Time O(N!) 
    Space O(N)
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(index, path, total):
            # find the target and save the path to result
            if total == target:
                result.append(path)
                return
            if total > target:
                return

            for i in range(index, len(candidates)):
                dfs(i, path + [candidates[i]], total + candidates[i])

        dfs(0, [], 0)
        return result
