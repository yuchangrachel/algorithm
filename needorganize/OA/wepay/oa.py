#1.Array Summarization
#Two lists l1 and l2, return true if sum of any two elements in l1 exists in l2.
def ArraySummarization(l1,l2):
    for n in l2:
        if isSum(l1, n):
            return True
    return False

def isSum(l1, target):
    visit = set()
    for n in l1:
        if target - n not in visit:
            visit.add(n)
        else:
            return True
    return False
print(ArraySummarization([1,3,2], [1,5]))


#2.Ada Lovelace Day: find the 2nd Tuesday of October
#举例：input是2018，output是9，因为10月9号是2018年10月的第二个周二。
