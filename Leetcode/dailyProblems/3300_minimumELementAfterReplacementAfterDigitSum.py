class Solution:
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []
        for i in range(n):
            sum = 0
            while nums[i] >0:
                digit = nums[i]%10
                sum = sum + digit
                nums[i] = nums[i] // 10
            arr.append(sum)
        return min(arr)



# No need to store in array, just maintaining minimum
class Solution:
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)
        minimum = float('inf')

        for i in range(n):
            sum = 0
            temp = nums[i]
            while temp >0:
                digit = temp%10
                sum = sum + digit
                temp = temp // 10
            minimum = min(sum,minimum)
        return minimum
