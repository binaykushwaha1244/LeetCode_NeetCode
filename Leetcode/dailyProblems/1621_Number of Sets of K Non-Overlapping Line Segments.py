
#

# tabulation
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        N = n+k-1
        dp = [[0] * (2*k +1) for _ in range(N+1)]

        for i in range(N+1):
            dp[i][0] =1

        for i in range(1,N+1):
            for j in range(1, min(i,2*k)+1):
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
        return dp[N][2*k]



# Memoization
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        N = n+k-1
        memo = {}

        def combination(i,j):

            if j > i:
                return 0
            # base case
            if j == 0 or j ==i:
                return 1
            
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = ( combination(i-1, j-1) + combination(i-1, j)) % MOD
        
            return memo[(i,j)]
        return combination(N,2*k)
