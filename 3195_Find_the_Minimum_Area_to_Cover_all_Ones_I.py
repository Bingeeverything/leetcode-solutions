class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        minrow, maxrow = m, -1
        mincol, maxcol = n, -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    minrow = min(minrow, i)
                    maxrow = max(maxrow, i)
                    mincol = min(mincol, j)
                    maxcol = max(maxcol, j)

        return (maxrow - minrow + 1) * (maxcol - mincol + 1)