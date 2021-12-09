#729. My Calendar I
'''
    TOPIC: intervals Two pointers, cannot overlap
    STEP: initially create intervals array, if can book succuessfully, add into intervals array
    WAYS:linearO(n)
'''
def __init__(self):
        self.booked = []

def book(self, start: int, end: int) -> bool:
        for a, e in self.booked:
            if max(a, start) < min(e, end): return False
        self.booked.append([start, end])
        return True


#731. My Calendar II
'''
    TOPIC: check if overlop twice in same intervals
    STEP:
    1.create overlap, arr two arrays, check if overlap, start < e and end > s
    2.[max(start,s), min(end, e)] mean [start, end] and [s, e] overlap subpart
'''
def __init__(self):
        self.overlap = []
        self.arr = []

def book(self, start: int, end: int) -> bool:
        for s, e in self.overlap:
            if start < e and end > s: return False
        
        for s, e in self.arr:
            if start < e and end > s:
                self.overlap.append([max(start, s), min(end, e)])
        self.arr.append([start, end])
        return True

