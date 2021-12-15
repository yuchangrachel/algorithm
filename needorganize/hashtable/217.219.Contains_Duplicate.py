# 217
def containsDuplicate(nums):
        if nums is None or len(nums) == 0: return False     
    # 1WAY hash table   
        dic = {}
        for x in nums:
            if dic.get(x) == 1:  # OR if dic.get(x) is not None:
                return True
            dic[x] = dic.get(x, 0) + 1
        return False
    
    #2 WAY set
    return len(set(nums)) != len(nums)

    # JS
    let seter = new Set(nums)
    return seter.size != nums.length

# 219
var containsNearbyDuplicate = function(nums, k) {
    if (nums == null || nums.length == 0) return false
    
    //create hash store {n:index}, next time see it, compare cur-index <= k or not
    const dic = new Map()
    for (let i = 0; i < nums.length; i++){
        if (dic.has(nums[i])){//has that key already
            if (Math.abs(i- dic.get(nums[i])) <= k) return true
        }
        //no key, add new pair; or update index
        dic.set(nums[i], i)
    }
    return false
};
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic.keys(): # check if meet <= k
                if abs(i - dic[nums[i]]) <= k: 
                    return True
            # add new pair or update
            dic[nums[i]] = i
        return False
        