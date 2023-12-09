class Solution:
    def hammingWeight(self, n: int) -> int:
        num = str(bin(n)[2:])
        return num.count('1')
