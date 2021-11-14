/*
121
LOGIC:
Only one time buy and sell(after buy)
1WAY:brute force O(n^2) TLE
2WAY:bottom-top dp, dp[i] = max_profix, option sell or keep T:O(n) S:O(n)
     when buy? default dp[0], will update if find smaller, than mean profit larger
3WAY:use profit variable, not extra space
*/
var maxProfit = function (prices) {
  if (prices == null || prices.length == 0) return 0;
  let dp = new Array(prices.length).fill(0);
  let buy = prices[0]; //cannot sell at this time, only can buy
  for (let i = 1; i < prices.length; i++) {
    dp[i] = Math.max(dp[i - 1], prices[i] - buy);
    //profit = Math.max(profit, prices[i] - buy)
    if (prices[i] < buy) buy = prices[i]; //update buy
  }
  return dp[prices.length - 1]; //profit
};

//122
//only need [i-1]&[i] compare neighbor accumulate neighbors
var maxProfit = function (prices) {
  if (prices == null || prices.length == 0) return 0;
  let profit = 0;
  let buy = prices[0];
  for (let i = 1; i < prices.length; i++) {
    if (prices[i] > prices[i - 1]) {
      //this is peak
      profit += prices[i] - prices[i - 1];
    }
  }
  return profit;
};
