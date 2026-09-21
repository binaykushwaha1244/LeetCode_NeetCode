class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0

        for i, ch in enumerate(s):
            reverse_value = ord('z') - ord(ch) + 1
            result += reverse_value * (i+1)
        return result


class Solution:
    def reverseDegree(self, s: str) -> int:
        ans, idx = 0,1

        for ch in s:
            ans += (ord('z') - ord(ch) + 1) * idx
            idx += 1
        return ans