class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 0
        ans = 0
        count = {}

        for i in range(n):
            count[s[i]] = count.get(s[i],0) +1
        
            while count[s[i]] > 2:
                count[s[j]] -= 1
                j +=1
            ans = max(ans, i-j+1)
        return ans

    