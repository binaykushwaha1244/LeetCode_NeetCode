class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)
        n = len(nums)
        if n != m+1:
            return False
        s = sorted(nums)
        
        for i in range(len(s)-1):
            if s[i] != i +1:
                return False
        if s[-1] != m:
            return False
        return True



from collections import Counter
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)
        count = Counter(nums)
        for i in range(1,m):
            if count[i] != 1:
                return False
        if count[m] != 2:
            return False
        return True
    


from collections import Counter
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)
        if len(nums) != m +1:
            return False
        count = Counter(nums)
        for number,frequency in count.items():
            if number != m:
                if frequency != 1:
                    return False
            else:
                if frequency !=2:
                    return False
        return True