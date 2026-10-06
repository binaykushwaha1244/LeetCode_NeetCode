class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0

        lower = set()
        upper = set()

        for ch in word:
            if ch.islower():
                lower.add(ch)
            else:
                upper.add(ch)
        for ch in lower:
            if ch.upper() in upper:
                count += 1
        return count 