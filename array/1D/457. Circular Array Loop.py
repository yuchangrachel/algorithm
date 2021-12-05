# 457. Circular Array Loop
def circularArrayLoop(self, nums: List[int]) -> bool:
        '''
TOPIC:Check if when Jump in array to check if any cycle inside 
TIME:O(N) SPACE:O(2*N)
STEP:
1.visited booean array. Iterate input array, create hashmap{cur:next} then while true loop see which is start point of loop. If next already in hashmap, return true
2.if find cur == next(same number) eg.[1,-1] or cur and next in different direction break
        '''
        n = len(nums)
        seen = [False] * len(nums)
        for i in range(len(nums)):
            if seen[i]: continue
            seen[i] = True
            # create hashmap store nums[cur]: next(one to one mapping), if exist, mean has loop
            hashmap = {}
            cur = i #assigin cur, since cur will update to next
            while True:
                nexter = ((cur + nums[cur]) % n + n) % n
                if cur == nexter or nums[cur] * nums[nexter] < 0: 
                    break 
                if nexter in hashmap: return True #if hashmap has nexter as key
                
                hashmap[cur] = nexter
                cur = nexter
                seen[nexter] = True
                
        return False
                