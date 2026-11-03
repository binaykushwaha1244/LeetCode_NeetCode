class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        mid = nums[n//2]
        moves = 0
        for i in range(n):
            moves += abs(nums[i] - mid)
        
        return moves



class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        mid = nums[n//2]
        moves = 0
        for i in range(n//2):
            moves += abs(nums[i] - mid)
            moves += abs(nums[n-i-1] - mid) 
        
        return moves





import random
from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        # STEP 1: Find the middle element using Quickselect
        def quickselect(k):

            left = 0
            right = len(nums) - 1

            while left < right:

                # STEP 2: Choose a random pivot
                pivot = nums[random.randint(left, right)]

                # STEP 3: Initialize two pointers
                i, j = left, right

                # STEP 4: Partition the array
                while i <= j:

                    while nums[i] < pivot:
                        i += 1

                    while nums[j] > pivot:
                        j -= 1

                    if i <= j:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                        j -= 1

                # STEP 5: Search only the required partition
                if k <= j:
                    right = j

                elif k >= i:
                    left = i

                else:
                    return nums[k]

            return nums[left]

        # STEP 6: Find the median
        n = len(nums)
        median = quickselect(n // 2)

        # STEP 7: Calculate minimum moves
        moves = 0

        for num in nums:
            moves += abs(num - median)

        return moves




class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        nums.sort()
        m = nums[n//2]
        return sum(nums[n//2:]) - sum(nums[:n//2]) -m*(n&1)


    