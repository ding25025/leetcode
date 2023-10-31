"""
    Given an m x n integer matrix matrix, if an element is 0, 
    set its entire row and column to 0's.
    Time - O(n^2)
    Space - O(2*k)
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        arr = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    arr.append([i, j])

        for k, l in arr:
            # each row to zero
            for r in range(row):
                matrix[r][l] = 0
            # each col to zero
            for c in range(col):
                matrix[k][c] = 0
