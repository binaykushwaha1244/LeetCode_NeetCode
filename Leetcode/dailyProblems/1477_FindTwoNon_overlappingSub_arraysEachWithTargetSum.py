class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        i = 0
        j = 0
        currSum = 0

        MinLenTillIdx = [float('inf')] * n
        bestMinLen = float('inf')
        result = float('inf')

        while j < n:
            currSum += arr[j]

            while currSum > target:
                currSum -= arr[i]
                i += 1

            if currSum == target:
                l = j - i + 1

                if i > 0 and MinLenTillIdx[i - 1] != float('inf'):
                    result = min(result, l + MinLenTillIdx[i - 1])

                bestMinLen = min(bestMinLen, l)

            MinLenTillIdx[j] = bestMinLen
            j += 1

        return -1 if result == float('inf') else result
    