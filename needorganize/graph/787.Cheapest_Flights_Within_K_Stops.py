# TLE
import heapq
class Solution:
    '''
    directed, weight graph 
    dijistra find minimum cost of paths to destination
    '''
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # create graph flight call 0-n-1, create 2d [start][dst] = cost
        graph = [[0 for j in range(n)] for i in range(n)]
        for flight in flights:
            graph[flight[0]][flight[1]] = flight[2]
        
        # use heap within K stops ascending oder
        minheap = []
        # sort first one(cost starting from 0), k+1mean include dest
        heappush(minheap, (0, src, k+1))
        
        while len(minheap) > 0:
            (price, place, remainstop) = heappop(minheap)
            
            if place == dst:
                return price
            
            if remainstop > 0:
                for i in range(n):
                    if graph[place][i] > 0: #has stop
                        heappush(minheap, (price + graph[place][i], i, remainstop-1))
        return -1