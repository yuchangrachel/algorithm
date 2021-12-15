def MaximumSum(self, A):
        '''
        TOPIC:find two numbers has same sum of all digits and find maximum result
        IDEA: heap(pq), hashmap
        HOW:
        heap for map
        find more than two numbers has same sum of all digits, so need to use priority queue find 2 largest number(minheap)
        when if len(ls), update answer, otherwise return -1
        '''
        dic = defaultdict(list)
        for n in A:
            sumdigit = self.sumdigit(n)
            heapq.heappush(dic[sumdigit], n)
            if len(dic[sumdigit]) > 2:
                heapq.heappop(dic[sumdigit])
        
        res = float('-inf')
        for k, v in dic.items():
            if len(v) == 2:
                res = max(res, sum(v))
        
        return res if res != float('-inf') else -1

def sumdigit(self, n):
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total