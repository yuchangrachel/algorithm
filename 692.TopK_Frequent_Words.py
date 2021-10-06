'''
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. 
Sort the words with the same frequency by their lexicographical order.
'''
# PYTHON KNOWLEDGE
# 1
# import heapq, heapq.heappush(minheap, (item0,item1)), sorted by item0, if item is string, will automatically sort by lexicographical order
# heapq.heappop(minheap)
# default is minheap, if maxheap, will heapq.heappush(minheap, -item)
# 2
# from collections import Counter
# dic = Counter(ls), Counter.items()

from collections import Counter
import heapq
def topKFrequent(words, k):
        # 1 WAY
        # if words is None or len(words) == 0: return []
        # wordCount = Counter(words)
        # h = []
        # for key, v in wordCount.items():
        #     heapq.heappush(h, (-v, key))
        # print(h)
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(h)[1])
        
        # return res

        
        # 2WAY
        # the:4 day:1 is:3 sunny:2
        dic = Counter(words)
        
        # store dict{word:freq} into minheap
        minheap = []
        # after add and heapify: day:1-> sunny:2 -> is:3 -> the:4
        for key in dic:
            heapq.heappush(minheap, (-dic[key], key)) #template: heappush(heap, (items0, item1)), items2:sortbase 

        i = 0
        res = []
        while i < k:
            freq, word = heapq.heappop((minheap))
            res.append(word) # pq, pop in the front
            i += 1
        
        return res
        
# print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is", "testing"], 4))
print(topKFrequent(["i","love","leetcode", "b", "b","i","love","coding"],2))#i not love