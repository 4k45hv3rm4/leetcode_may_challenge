def firstBadVersion(n) :
    i=0
    flag=0
    for i in range(n,-1,-1):
        if isBadVersion(i):
            pass
        else:
            return i+1
    return flag;
