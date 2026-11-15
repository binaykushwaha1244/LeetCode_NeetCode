class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        curr_sum = 0
        even_sum = 0
        odd_sum = 0
        res = 0

        MOD = 10**9 + 7

        for n in arr:
            curr_sum += n

            if curr_sum % 2:
                res = (res + 1 + even_sum) % MOD
                odd_sum += 1
                
            else:
                res = (res + odd_sum) 
                even_sum += 1
        return res
