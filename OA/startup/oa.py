'''
# 1.String problem
"aaabbbaaa"=> aaa,bbb,aaa, three blocks already in same length, so 0
"ababb"=> a,b,a,bb, four blocks, need let them in same length, max:2, a(1),b(1),a(1),bb(0), so total is 3

LOGIC:
two pointer
'''
def blocks(S):
    blocks = [] 
    count = 0
    max_c = 0
    j = 0
    for i in range(len(S)):
        if S[i] == S[j]:
            count+=1
            max_c = max(count, max_c)
        else:
            blocks.append(count)
            count = 1
            j = i
    
    if i == len(S) - 1 and count != 0:
        blocks.append(count)
    res = 0
    for block in blocks:
        res += (max_c - block)
        
    return res

print(blocks("babaa"))


'''
2.SQL
department table: dept_id,departmentname
employee table: dept_id, peoplename, salary
return: dept_id, countPeople, salaryACCum

select d.dept_id,count(*), sum(e.salary)
from department d inner join employee e on d.dept_id=e.dept_id group by d.dept_id
ORDER BY d.dept_id ASC
'''
