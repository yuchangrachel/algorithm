/*
TOPIC:one transaction, buy first, and sell another day
STEP:1DP with size n
*/
var maxProfit = function(prices) {
    const dp = new Array(prices.length).fill(0)
    let buy = prices[0]
    let res = 0
    for (let i = 1; i < prices.length; i++){
        dp[i] = Math.max(prices[i] - buy, 0)
        if (prices[i] < buy){
            buy = prices[i]
        }
        res = Math.max(dp[i],res)
    }
    return res
};