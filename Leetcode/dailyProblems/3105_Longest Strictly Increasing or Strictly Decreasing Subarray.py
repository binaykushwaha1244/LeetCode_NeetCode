class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            curr = []
            for j in range(i,n):
                curr.append(nums[j])
                if(all(curr[idx] > curr[idx-1] for idx in range(1,len(curr))) or
                    all(curr[idx] < curr[idx-1] for idx in range(1,len(curr)))
                    ):
                    res = max(res, j-i+1)
        return res




class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc,dec,ans = 1,1,1

        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                inc += 1
                dec = 1
            elif nums[i-1] < nums[i]:
                dec += 1
                inc = 1
            else:
                dec = 1
                inc = 1

            ans = max(inc,dec,ans)
        return ans