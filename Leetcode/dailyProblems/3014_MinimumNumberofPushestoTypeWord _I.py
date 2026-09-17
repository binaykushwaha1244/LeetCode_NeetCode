class Solution:
    def minimumPushes(self, word: str) -> int:
        mp = {}
        for ch in word:
            mp[ch] = mp.get(ch,0) + 1
        
        arr = sorted(mp.items(), key = lambda x:x[1], reverse = True)

        assign_key = 2
        result= 0
        push = 1

        for ch,freq in arr:
            result += freq * push
            assign_key += 1

            # we have used all 8 keys
            if assign_key > 9:
                assign_key = 2
                push += 1

        return result




class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26

        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        freq.sort(reverse=True)

        result = 0
        for i, f in enumerate(freq):
            result += f * (i//8 + 1)
        return result
