class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0: #while n:
            res += n % 2
            n = n >> 1 #bit shif it to right by 1
        
        return  res