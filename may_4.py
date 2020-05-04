class Solution:
    def findComplement(self, num: int) -> int:
        #to get number of bits
        c = int((math.log(num))/math.log(2)+1)
        #to get one's complement
        return ((1<<c)-1)^num

