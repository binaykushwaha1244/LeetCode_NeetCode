class Solution:
    def reverse(self, nums,left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        k = k%n
        nums.reverse()
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
        


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        if k != 0:
            arr = nums[n-k:]
            del nums[n-k:]
            nums[0:0] = arr
