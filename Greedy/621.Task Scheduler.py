'''
    LOGIC:Greedy+hashmap most freq need do task earlier
    STEP:
    A:3 B:3 C:1 n=2
    A--A--A
    ABCAB-AB
    leftslot=(3-1)*2=4[-1miss last]
    if A continue, ifB 4-(3-1)=2[miss last]
    1.create hashmap, find mostChar,mostfreq
    2.create leftslot=(mostfreq-1)*2
    3.iterate map, if see k=mostchar,doing task; if seev=mostfreq,leftslot -= (v-1) else leftslot -=v
    if leftslot <= 0 nothingleft return len(task)
    else: still leftslot return len(task)+leftslot
'''
def leastInterval(self, tasks: List[str], n: int) -> int:
        mostChar = tasks[0]
        mostFreq = 0
        mapping = collections.defaultdict(int)
        for task in tasks:
            mapping[task] += 1
            if mapping[task] > mostFreq:
                mostFreq = mapping[task]
                mostChar = task
        
        leftslot = (mostFreq - 1) * n
        for k, v in mapping.items():
            if k == mostChar:
                continue
            elif v == mostFreq:
                leftslot -=(v-1)
            else:
                leftslot -= v
            
        if leftslot <= 0: 
            return len(tasks)
        else:
            return len(tasks) + leftslot