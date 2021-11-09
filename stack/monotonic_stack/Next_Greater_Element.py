# 496. Next Greater Element I
def nextGreaterElement(nums1,nums2):
        if not nums1 or not nums2: return []
        '''
        Monotonic stack
        TIME: O(n)
        store decreasing ele in stack, if need cur > peek(), handle larger
        create map for {n:first greater} for nums1
        traverse nums2, create and updating stack
        All integers in nums1 and nums2 are unique.=> use dict
        '''
        stack = []
        dic = {}
        res = []
        for n in nums2:
            while len(stack) > 0 and stack[-1] <n:
                top = stack.pop()
                dic[top] = n
            stack.append(n)
            
        for n in nums1:
            if n not in dic:
                res.append(-1)
            else:
                res.append(dic[n])
        
        return res
    
        '''
        Brute Force:
        TIME:O(n^2)
        '''
        # res = [-1] * len(nums1)       
        # for j in range(len(nums1)):
        #     n = nums1[j]
            
        #     flag = False
        #     findindex = nums2.index(n)

        #     for i in range(findindex+1, len(nums2)):
        #         if nums2[i] > n:
        #             flag = True
        #             res[j] = nums2[i]
        #             break
        #     if flag == False:
        #         res[j] = - 1
        
        # return res

# 503. Next Greater Element II     
def nextGreaterElements(nums):
        '''
        1WAY BRUTE FORCE
        O(n^2)
        '''
#         n = len(nums)
#         res = [-1] * n
        
#         for i in range(n):
#             for j in range(i+1, i+n): #dont need n+n, only need i+extra n
#                 if nums[j%n] > nums[i]:
#                     res[i] = nums[j%n]
#                     break # if assign to res, cannot update later
#         return res
        
        '''
        LOGIC:
        This problem given circular integer array 
        use strictly decreasing stack
        This input array include duplicate nums, so stack store index,not val
        TIME:O(N)
        '''
        n = len(nums)
        if not nums or n == 0: return []
        
        stack = []
        res = [-1] * n
        
        for i in range(n * 2):
            i = i % n
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            if i < n: stack.append(i)
        
        return res
        

# print(nextGreaterElements([100,1,11,1,120,111,123,1,-1,-100]))  #[120,11,120,120,123,123,-1,100,100,100]

#556. Next Greater Element III
def nextGreaterElement3(n):
        '''
        number permutation, find the permutation that samllest larger than n
        1 2 443322->1 3 222344
        see pattern, see peak and decreasing(443322), traverse from back, now find 2(need be swaped)
        Swap with the first number larger than 2 starting from back
        then sorted rest of list
        '''
        strN = list(str(n))
        i = len(strN) - 1
        #1step find the num at one index need swap
        for i in range(len(strN) - 1, 0, -1):
            if int(strN[i]) > int(strN[i-1]): #find strN[i-1]
                break

        #2step find the first greater one at one index, swap with find at that index
        for j in range(len(strN) - 1, i-1, -1): #include i
            if int(strN[i-1]) < int(strN[j]):
                #now swap
                strN[i-1], strN[j] = strN[j], strN[i-1]
                break

        #3step combine,sort rest of list after greater index
        ls = sorted(strN[i:])
        res = int("".join(strN[:i] + ls))
        if n < res and res < 2**31:    
            return res
        else:
            return -1
        # return res if n < res < (2**31) else -1
        
print(nextGreaterElement3(2147483476))