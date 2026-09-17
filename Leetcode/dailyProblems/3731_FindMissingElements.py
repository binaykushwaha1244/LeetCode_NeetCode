class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = min(nums)
        large = max(nums)
        ans = []

        for i in range(small, large+1):
            if i not in nums:
                ans.append(i)
        return ans


# use set
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = min(nums)
        large = max(nums)
        seen = set(nums)
        ans = []

        for i in range(small, large+1):
            if i not in seen:
                ans.append(i)
        return ans


# list comprehension

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [x for x in range(min(nums),max(nums)+1) if x not in s]