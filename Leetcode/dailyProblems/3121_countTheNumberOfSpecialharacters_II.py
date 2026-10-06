class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        lastLower = {}
        firstUpper = {}

        for i,c in enumerate(word):
            if c.islower(): lastLower[c] = i
            elif not c in firstUpper:
                firstUpper[c] = i
        
        res = 0

        for i in range(26):
            c = chr(i + ord('a'))
            if (c in lastLower and c.upper() in firstUpper and lastLower[c] < firstUpper[c.upper()]):
                res += 1
        return res


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower= [-1]*26
        first_upper = [len(word)]*26

        for i,ch in enumerate(word):
            if ch.islower():
                index = ord(ch) -ord('a')
                last_lower[index] = i
            else:
                index = ord(ch) - ord('A')
                first_upper[index] = min(first_upper[index],i)
        count = 0

        for i in range(26):
            if last_lower[i] != -1 and first_upper[i] != len(word):
                if last_lower[i] < first_upper[i]:
                    count += 1
        return count