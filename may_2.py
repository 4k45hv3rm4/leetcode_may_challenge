class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        x=0
        for i in J:
            x+=S.count(i)
        return  x
