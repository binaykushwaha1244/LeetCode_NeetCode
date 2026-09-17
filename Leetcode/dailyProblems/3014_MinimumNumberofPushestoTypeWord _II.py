class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0]*26

        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        
        freq.sort(reverse=True)
        result = 0

        for i,f in enumerate(freq):
            result += f * (i //8 + 1)
        return result




class Solution:
    def minimumPushes(self, word: str) -> int:
        frequencies = sorted(Counter(word).values(), reverse = True)

        res = 0
        for i, freq in enumerate(frequencies):
            press = (i // 8) + 1
            res += freq * press
        return res