'''
    TOPIC:Sort by height and other infor" k people in front higher/equal"
    STEP:
    1.if same height, sort[1] increase, if not same height, sort[0] decrease
    2.create res array insert subarray base on [1]
'''
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if people is None or len(people) == 0: return []
        res = []
        people.sort(key=lambda x:x[1]) # consider same height, then sort [1] increasing
        people.sort(key=lambda x:-x[0]) # sort height decreasing
        
        for p in people:
            res.insert(p[1], p)
        
        return res
        