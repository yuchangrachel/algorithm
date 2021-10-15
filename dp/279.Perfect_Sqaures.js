/*
dp[0] = 0 
dp[1] = dp[0]+1 = 1
dp[2] = dp[1]+1 = 2
dp[3] = dp[2]+1 = 3
dp[4] = Min{ dp[4-1*1]+1, dp[4-2*2]+1 } 
      = Min{ dp[3]+1, dp[0]+1 } 
      = 1				
dp[5] = Min{ dp[5-1*1]+1, dp[5-2*2]+1 } 
      = Min{ dp[4]+1, dp[1]+1 } 
      = 2
						.
						.
						.
dp[13] = Min{ dp[13-1*1]+1, dp[13-2*2]+1, dp[13-3*3]+1 } 
       = Min{ dp[12]+1, dp[9]+1, dp[4]+1 } 
       = 2
						.
						.
						.
dp[n] = Min{ dp[n - i*i] + 1 },  n - i*i >=0 && i >= 1

LOGIC:
1.Who is perfect square: 1 and other numbers'square
2.need least number of perfect square
bottom-top dp
*/
var numSquares = function (n) {
  if (n == 0) return 0;
  //create dp dp[i] means least square need for i number
  const dp = new Array(n + 1).fill(n); //size:n+1. fill by n(maxi val in this question)
  //init dp
  dp[0] = 0;
  dp[1] = 1; //count itself
  dp[2] = dp[1] + 1; //+1 count itself
  dp[3] = dp[2] + 1;

  for (let i = 4; i <= n; i++) {
    for (let j = 1; j * j <= i; j++) {
      dp[i] = Math.min(dp[i - j * j] + 1, dp[i]);
    }
  }
  return dp[n];
};
