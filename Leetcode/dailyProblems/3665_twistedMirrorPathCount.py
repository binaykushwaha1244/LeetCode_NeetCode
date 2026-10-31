from typing import List
# recursion
class Solution:
    LEFT = 0
    UP = 1
    MOD = 10**9 + 7

    def solve(self, grid, i, j, camefrom, t):
        # Out of bounds
        if i >= self.m or j >= self.n:
            return 0

        # Destination reached
        if i == self.m - 1 and j == self.n - 1:
            return 1

        # Memoization
        if t[i][j][camefrom] != -1:
            return t[i][j][camefrom]

        # Mirror cell
        if grid[i][j] == 1:
            if camefrom == self.LEFT:
                t[i][j][camefrom] = self.solve(
                    grid, i + 1, j, self.UP, t
                )
            else:
                t[i][j][camefrom] = self.solve(
                    grid, i, j + 1, self.LEFT, t
                )

            return t[i][j][camefrom]

        # Normal cell
        totalcount = 0

        totalcount = (
            totalcount + self.solve(grid, i + 1, j, self.UP, t)
        ) % self.MOD

        totalcount = (
            totalcount + self.solve(grid, i, j + 1, self.LEFT, t)
        ) % self.MOD

        t[i][j][camefrom] = totalcount

        return t[i][j][camefrom]

    def uniquePaths(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        # 3D DP: m x n x 2
        t = [[[-1, -1] for _ in range(self.n)]
             for _ in range(self.m)]

        return self.solve(grid, 0, 0, self.LEFT, t)