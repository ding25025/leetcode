"""
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
    return the number of islands.
    Time O(M X N)
    Space O(M X N)
    **BFS**
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        islands = 0
        visited = set()
        queue = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            queue.append((r, c))

            while queue:
                pos = queue.popleft()
                row, col = pos[0], pos[1]

                for r_offset, c_offset in directions:
                    if (
                        row + r_offset < 0
                        or row + r_offset >= rows
                        or col + c_offset < 0
                        or col + c_offset >= cols
                        or grid[row + r_offset][col + c_offset] != "1"
                        or (row + r_offset, col + c_offset) in visited
                    ):
                        continue
                    visited.add((row + r_offset, col + c_offset))
                    queue.append((row + r_offset, col + c_offset))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
        return islands
