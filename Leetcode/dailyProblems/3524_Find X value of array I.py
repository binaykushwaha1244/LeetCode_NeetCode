class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)

        result = [0] * k
        prevCount = [0] * k

        for i in range(n):

            # Subarrays ending at index i
            currCount = [0] * k

            currElementRemainder = nums[i] % k
            currCount[currElementRemainder] += 1

            for oldRem in range(k):
                newRemain = (oldRem * nums[i]) % k

                currCount[newRemain] += prevCount[oldRem]

            prevCount = currCount

            for x in range(k):
                result[x] += prevCount[x]

        return result
    