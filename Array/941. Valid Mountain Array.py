'''
    TOPIC:traverse array
    STEP:1WAY:extra variable. 2WAY:only while loops
    '''
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        N = len(arr)
        
        while i+1 < N and arr[i] < arr[i+1]:
            i += 1
        
        if i == 0 or i == N-1: # only decreasing or only increasing
            return False
        
        while i+1 < N and arr[i] > arr[i+1]:
            i += 1
        return i == N-1
        
        
        #1WAY
#         climbUp = False
#         climbDown = False
#         peak = -1
#         for i in range(1,len(arr)):
#             if arr[i] > arr[i-1]:
#                 climbUp = True
#             else:
#                 peak = i-1
#                 break
#         if climbUp == False:
#             return False
        
#         for i in range(peak, len(arr)-1):
#             if arr[i] > arr[i+1]:
#                 climbDown = True
#             else:
#                 return False
#         if climbDown == False:
#             return False
#         return True
        
        
print(validMountainArray([0,3,2,1]))