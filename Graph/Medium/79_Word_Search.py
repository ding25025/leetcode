"""
    Given an m x n grid of characters board and a string word, 
    return true if word exists in the grid.
    Time O(M X N)
    Space O(1)
    **DFS**
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(r, c, count):
            if r < 0 or r == m or c < 0 or c == n:
                return False
            if board[r][c] != word[count] or board[r][c] == "V":
                return False
            if count == len(word) - 1:
                return True
            temp = board[r][c]
            board[r][c] = "V"
            result = (
                dfs(r + 1, c, count + 1)
                or dfs(r - 1, c, count + 1)
                or dfs(r, c + 1, count + 1)
                or dfs(r, c - 1, count + 1)
            )
            board[r][c] = temp

            return result

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
