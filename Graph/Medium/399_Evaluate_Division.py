"""
    [399. Evaluate Division](https://leetcode.com/problems/evaluate-division/description/)

    Time O(E+V)
    Space O(N)
"""


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        """
        a/b = 2; b/a = 1/2
        b/c = 3; c/b = 1/3
        a/c = a/b * b/c = 2 * 3 = 6

        """
        # Construct graph
        edge = defaultdict(dict)
        for idx, (src, dest) in enumerate(equations):
            edge[src][dest] = values[idx]
            edge[dest][src] = 1 / values[idx]
        print(edge)

        def dfs(src, dest, visited):
            if src not in edge or dest not in edge:
                return -1

            if dest in edge[src]:
                return edge[src][dest]

            for i in edge[src]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i, dest, visited)
                    if temp == -1:
                        continue
                    else:
                        return temp * edge[src][i]
            return -1

        # go through each queries
        result = []
        for i, j in queries:
            result.append(dfs(i, j, set()))
        return result
