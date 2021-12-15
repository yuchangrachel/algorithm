# 599. Minimum Index Sum of Two Lists
'''
    LOGIC: Intersection Problem
    1.hashmap store list1
    2.if map match with list2, store res
    3.result store minsum
    TIME COMPLEXITY: T:O(N) S:O(N)
'''
def findRestaurant1(list1, list2):
        if not list1 or not list2: return []
        
        dic = {}
        min_sum = float('inf')
        res = []
        result = []
        for i in range(len(list1)):
            dic[list1[i]] = i
        
        for i in range(len(list2)):
            if list2[i] in dic.keys(): # has intersection
                res.append((list2[i], dic[list2[i]] + i)) # add tuple
                min_sum = min(min_sum, dic[list2[i]] + i)
        
        print("min: ", min_sum)
        for k, v in res:
            print("k ", k, " ", v)
            if v == min_sum:
                result.append(k)
    
        return result

def findRestaurant2(self, list1: List[str], list2: List[str]) -> List[str]:
        if not list1 or not list2: return []
        
        min_sum = float('inf')
        res = []
        
        dic = {word:i for i, word in enumerate(list1)}
        
        
        for i in range(len(list2)):
            if list2[i] in dic.keys(): # has intersection
                res.append((list2[i], dic[list2[i]] + i)) # add tuple
                min_sum = min(min_sum, dic[list2[i]] + i)

        return [k for k, v in res if v == min_sum]
        
print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Shogun","Burger King"]))