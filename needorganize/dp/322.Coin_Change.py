#322. Coin Change
def coinChange(self, coins: List[int], amount: int) -> int:
        #TOPIC:fewest number of coin to make up 'amount'
        #HOW:bottom-top dp
        
        if amount == 0: return 0
        #dp store each index mean different amount has fewest number of coins can be maked up to current amount
        #CREATE DP ARRAY
        dp = [amount+1] * (amount+1) 
        #INIT DP
        dp[0] = 0 #0amount need 0 coin
        for i in range(1,amount+1):#amount=11
            for j in range(0, len(coins)):#coin:5
                if coins[j] <= i:
                    #TRASFER FUNCTION
                    dp[i]=min(dp[i], dp[i-coins[j]] + 1) #dp[11],dp[6](subproblem)
        return -1 if dp[amount]>amount else dp[amount]