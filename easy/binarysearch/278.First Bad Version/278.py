def firstBadVersion(n):
    if n == 0: return 0
    low = 1
    high = n
    while low < high:
        mid = int((low+high) /2)  # OR (low + high) //2
        if isBadVersion(mid):
            high = mid 
        else:
            low = mid + 1
    if high != -1:
        return high
    else:
        return -1
        