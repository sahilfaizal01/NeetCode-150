class Solution:
    def hammingWeight(self, n: int) -> int:
        num = str(bin(n)[2:])
        return num.count('1')
        ## solution 2 - right shift technique
        res = 0
        while n>0:
            res += n%2 # remainder
            n = n >> 1 # right shift
        return res
        # solution 3 - using AND operation
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res




