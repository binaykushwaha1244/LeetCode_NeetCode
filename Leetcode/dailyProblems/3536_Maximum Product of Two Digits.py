class Solution:
    def maxProduct(self, n: int) -> int:
        arr = []
        while n> 0:
            digit = n % 10
            arr.append(digit)
            n = n //10
        
        arr.sort()
        return arr[-1] * arr[-2]
    