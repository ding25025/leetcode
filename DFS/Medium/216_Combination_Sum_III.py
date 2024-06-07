"""
- Only numbers 1 through 9 are used.
- Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, 
and the combinations may be returned in any order.
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def dfs(start, path, currSum):
            if len(path) == k and currSum == n:
                result.append(path)
                return
            elif len(path) == k and currSum != n:
                return

            for i in range(start, 10):
                dfs(i + 1, path + [i], currSum + i)

        dfs(1, [], 0)

        return result
