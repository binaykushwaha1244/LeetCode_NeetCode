class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        original = n
        while True:
            prod = 1
            temp = original
            while temp > 0:
                digit = temp%10
                prod *= digit
                temp //= 10

            if prod % t == 0:
                return original
            original = original+1
            