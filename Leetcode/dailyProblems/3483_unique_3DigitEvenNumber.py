class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        s = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if (i==j or i==k or j==k):
                        continue
                    num = digits[i]*100 + digits[j]*10 + digits[k]

                    if num >= 100 and num%2 ==0:
                        s.add(num)
        # result= list(s)
        # return sorted(result)
        return len(s)

# Time complexity: O(n**3)



class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        result = []
        count = {i: 0 for i in range(10)}
        
        for digit in digits:
            count[digit] += 1

        for i in range(1,10):
            if count[i] == 0:
                continue

            count[i] -= 1
            for j in range(10):
                if count[j] == 0:
                    continue
                count[j] -= 1
                for k in range(0,10,2):
                    if count[k] == 0:
                        continue
                    count[k] -= 1

                    num = i*100 + j*10 +k
                    result.append(num)

                    count[k] += 1

                count[j] +=1

            count[i] +=1

        return len(result)

# Time Complexity : O(9 * 10 * 5) O(n)
