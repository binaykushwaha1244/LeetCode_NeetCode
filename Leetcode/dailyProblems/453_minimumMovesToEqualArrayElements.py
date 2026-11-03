class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)

        steps = 0
        mini = min(nums)

        for i in range(n):
            steps += nums[i] - mini
        
        return steps


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)

        steps = 0
        mini = min(nums)

        summ = sum(nums)

        return summ - n*mini
