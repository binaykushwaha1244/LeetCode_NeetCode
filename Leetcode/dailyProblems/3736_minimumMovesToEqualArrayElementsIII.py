class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)
        maxi = max(nums)
        moves = 0
        for i in range(n):
            moves += maxi - nums[i]
        return moves