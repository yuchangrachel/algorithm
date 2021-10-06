def containsNearbyAlmostDuplicate(nums,k,t):
        if nums is None or len(nums) < 2: return False
        # 1WAY brute force TLE two loop O(n^2)    
        # for i in range(0, len(nums)):
        #     for j in range(i+1, i+k+1):
        #         if j < len(nums):
        #             if abs(nums[i]-nums[j]) <= t:
        #                 return True

        # 2WAY BUCKET SORT
        # refer;https://leetcode.com/problems/contains-duplicate-iii/discuss/824578/C%2B%2B-O(N)-time-complexity-or-Explained-or-Buckets-or-O(K)-space-complexity
        # two conditions: -t<=num diff<=t and -k<=index diff<=k 
        # divide buckets by t+1 range, each key = num /(t+1) , why t+1 since avoid t maybe 0 /0(error)
        '''
        [1,5,2,4,3,9,1,5,9], k = 2, t = 3

1 // (3+1) = 0
5 // (3+1) = 1
2 // (3+1) = 0
4 // (3+1) = 1
3 // (3+1) = 0
9 // (3+1) = 2

Here, Bucket[0] will contain numbers 0,1,2,3.
Bucket[1] will contain numbers 4,5,6,7.
Bucket[2] will contain numbers 8,9,10,11.

On observing carefully, we can see that the absolute difference
between any two numbers in any bucket is at most t, which is what we want.

Also, there can be a case where the neighbouring bucket has some number
whose absolute difference with a number in the current bucket is at most t.
For instance, 2 lies in Bucket[0] and 4 lies in Bucket[1] and 4 - 2 = 2 < 3 (=t).
This can only happen in neighbouring buckets. Therefore, we need to check for this too.
        '''
        if t < 0: return False
        buckets = {}
        w = t+1
        for i in range(len(nums)):
            key = nums[i] // w
            
            if key in buckets \
            or key - 1 in buckets and abs(buckets[key-1] - nums[i]) < w \
            or key + 1 in buckets and abs(buckets[key+1] - nums[i]) < w: return True
            
            buckets[key] = nums[i]
            
            if i>= k: del buckets[nums[i-k] // w]  # or len(buckets) > k
            
        return False
             
# print(containsNearbyAlmostDuplicate([1,2,3,1],3, 0))
print(containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))

