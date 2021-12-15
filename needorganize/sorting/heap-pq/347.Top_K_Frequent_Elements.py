# USE HEAP
# see top k, think about heap pq minheap O(nlogk)
# return k nums who most frequent,if k=2, will have two two top.
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
	#1 WAY
	dic = collections.Counter(nums)
        return heapq.nlargest(k, dic, key=lambda k:dic[k])
        
        #2 WAY
        if nums is None or len(nums) == 0 or k == 0: return []
        
        # create hash store{num:freq}
        dic = Counter(nums)
        minheap = []
        
        for key in dic:
            heappush(minheap, (dic[key], key))
            if len(minheap) > k:
                heappop(minheap)
        
        # display res, return any order
        res = []
        while len(minheap) > 0:
            freq, num = heappop(minheap)
            res.append(num)
        
        return res
        
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        minheap = []
        res = []
        count = collections.Counter(nums)
        for key, v in count.items():
            heappush(minheap, (v, key))
            
            if len(minheap) > k:                
                heappop(minheap)
        
        while len(minheap) > 0:
            res.append(heappop(minheap)[1])
        
        return res
        

# USE SORTING + HASHTABLE
# O(nlogn)
//hash{n:freq}
//sortedlist sort based hash's freq
//reslist push hash's n from back(pop) until reach k size
var topKFrequent = function(nums, k) {
    if (nums== null || nums.length == 0 || k == 0) return []
    
    //create hash store freq
    const hash = new Map()
    for (let n of nums){
        hash.set(n, (hash.get(n) || 0) + 1)
    }
    
    //freqlist [{}] store map
    const freq = []
    for (const [k, v] of hash){
        freq.push({n: k, count: v})
    }
    
    //sort freqlist
    freq.sort((a,b) => a.count - b.count)
    
    //pop k in freqlist store reslist
    const res = []
    while (res.length < k){
        res.push(freq.pop().n)
    }
    return res
};

        
