class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans = []

        for i in range(len(nums)):
            nums[i] = str(nums[i])
            ans.extend([int(x) for x in nums[i]])  # extend takes the element from the other list and adds them one by one
        return ans