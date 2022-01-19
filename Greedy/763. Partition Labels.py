'''
    TOPIC:Interval(make groups), same letter must in same group, result push len of group
    STEP:
    create hashmap{ch:latestindex}(one pass).second pass compare i and farthest, mapping[s[i]].need start var
    '''
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        # create hashmap store {ch:lastestindex}
        mapping = collections.defaultdict(int)
        for i in range(len(s)):
            mapping[s[i]] = i
        
        farthest = mapping[s[0]]
        start = 0
        for i in range(1,len(s)):
            if i <= farthest:
                farthest = max(farthest, mapping[s[i]])
            else:
                res.append(farthest - start + 1)
                start = i
                farthest = mapping[s[i]]
        #fast group
        res.append(farthest - start + 1)
        return res
            