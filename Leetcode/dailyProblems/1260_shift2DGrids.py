class Solution:
    def reverse(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        arr = []

        # for row in grid:
        #     for x in row:
        #         arr.append(x)
        arr = [x for row in grid for x in row]
        n = len(arr)
        cols = len(grid[0])
        k = k%n

        arr.reverse()
        self.reverse(arr,0,k-1)
        self.reverse(arr,k,n-1)
        grid = [arr[i:i+cols] for i in range(0, len(arr), cols)]
        return grid




# Trick

# in an 1D array
# when i = 6
# but i 2D array the its position can be found by 
# grid[row] [col] = 
#  row = i//col  = 6//3 = 2
# col = i% col  = 6%3 = 0
# in position [2][0]

# n = rows * cols




class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows = len(grid)
        cols = len(grid[0])
        n = rows * cols

        k %= n

        if k == 0:
            return grid

        def reverse(left, right):
            while left < right:
                r1, c1 = left // cols, left % cols
                r2, c2 = right // cols, right % cols

                grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]

                left += 1
                right -= 1

        # Same 3-reversal method as LeetCode 189
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

        return grid