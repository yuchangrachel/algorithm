//two directions:right&down, starting from left top to bottom right. two options, choose minimum health points, so consider dp
//Must confirm each cell's power must >= 1, so can think backword, end point to start point
//here is bottom-top dp
var calculateMinimumHP = function (dungeon) {
  if (dungeon == null || dungeon.length == 0) return 0;

  let m = dungeon.length;
  let n = dungeon[0].length;
  //create dp
  //dp 2d array size is row+1, col+1
  const dp = new Array(m + 1).fill(Infinity);
  for (let i = 0; i < dp.length; i++) {
    dp[i] = new Array(n + 1).fill(Infinity);
  }

  //init dp
  dp[m][n - 1] = 1; //down
  dp[m - 1][n] = 1; //right
  for (let i = m - 1; i >= 0; i--) {
    for (let j = n - 1; j >= 0; j--) {
      //need health point less
      let need = Math.min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j];
      dp[i][j] = need <= 0 ? 1 : need;
    }
  }
  return dp[0][0];
};
