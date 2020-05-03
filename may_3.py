class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        flag=0
        if ransomNote=='':
            flag=1
        if ransomNote==magazine:
            flag=1
        for i in ransomNote:
            if  magazine.count(i) >= ransomNote.count(i) :
                flag = 1
            else:
                flag=0
                break
        if flag:
            return True
        else:return False
