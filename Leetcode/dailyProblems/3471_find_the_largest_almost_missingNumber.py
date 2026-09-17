class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = [0] * 51

        for i in range(n - k + 1):
            seen = [False] * 51

            for j in range(i, i + k):
                if not seen[nums[j]]:
                    count[nums[j]] += 1
                    seen[nums[j]] = True

        ans = -1

        for x in range(51):
            if count[x] == 1:
                ans = x

        return ans