class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        c = []
        n = k
        for i in num:
            while n and c and c[-1]>i:
                c.pop()
                n=n-1
            c.append(i)
        res = "".join(c[0:len(num)-k]).lstrip("0")
        if len(res):
            return res
        else:
            return "0"
