#414. Third Maximum Number
def thirdMax(nums):
        ''''
        LOGIC: 3rd max ... use HEAP(minheap as default heap)
        HOW:
        NOT NEED minheap knowledge
        if minheap size < 3, mean return maxOne which is minheap[-1]
        ATTENTION: has duplicates in nums, but heap only store k distinct elements: use set avoid duplicate, but hard to use heap(list) and set at the same time.heapify set not affect heap. So use basic idea: sort set(nums) reversely, if set.size < 3 return max;other return [0]
        TIME: O(nlogn)
        '''
        if not nums or len(nums) == 0: return -1
        
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums) < 3: return nums[0]
        else: return nums[2]
        
print(thirdMax([1,2,2,5,3,5]))  #1,2,3,5 => 5,3,2,1 => [2]