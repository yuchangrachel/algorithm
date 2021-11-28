# 594. Longest Harmonious Subsequence
def findLHS(self, nums: List[int]) -> int:
        # TOPIC: need to get longest subquence which diff is only 1, which mean need sort, compare neighbor
        # HOW: 1.use hashmap store(n:freq), create array only store unique and also sort, then traverse array, sum up hashmap vaL

        #2WAY single loop SPACE: O(n) TIME:O(N)
        if not nums or len(nums) == 0: return 0
        dic = collections.defaultdict(int)
        longest = 0
        
        for n in nums:
            dic[n] += 1
            if n+1 in dic:
                longest = max(longest, dic[n] + dic[n+1])
            if n-1 in dic:
                longest = max(longest, dic[n] + dic[n-1])
        return longest
                
        
        #1WAY brute force
        # TIME: O(nlogn) SPACE: O(2N)        
#         if not nums or len(nums) == 0: return 0
        
#         counter = collections.Counter(nums)
#         arr = []
#         for n in nums:
#             if n not in arr:
#                 arr.append(n)
#         arr.sort()
        
#         longest = 0
#         for i in range(1, len(arr)):
#             if arr[i] - arr[i-1] == 1:
#                 temp = counter[arr[i]] + counter[arr[i-1]]
#                 longest = max(longest, temp)
#         return longest