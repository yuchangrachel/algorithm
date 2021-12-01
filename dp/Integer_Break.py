# 343. Integer Break
def IntegerBreak(n): #4(1,3; 2,2; 3,1)
    dp = [1] * (n+1)
    
    for i in range(1, n+1,1):
        largest = 1
        for j in range(1,i,1):
            f1 = max(j, dp[j])
            f2 = max(i-j, dp[i-j])
            print(j, " ", dp[j])
            largest = max(largest, f1*f2)
        
        dp[i] = largest
    
    return dp[n]

print(IntegerBreak(4))

'''
i=2
j=1, f1=(1,dp[1])=1 f2=(1,dp[1])=1
i=3
j=1 f1:1 f2:2
j=2 


'''