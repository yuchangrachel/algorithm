//198. House Robber
//[2,1,1,2] => 4, so mean rob not just compare[i-1][i-2], actually see max profit
var rob = function (nums) {
  if (nums == null || nums.length == 0) return 0;
  //two option:rob or not rob -> result separate subproblem -> get MAX value: use dp(bottom-top)
  const dp = new Array(nums.length).fill(0);
  //   let profit = 0;
  dp[0] = nums[0];
  if (nums.length == 1) return dp[0];
  dp[1] = Math.max(dp[0], nums[1]);
  if (nums.length == 2) return dp[1];

  for (let i = 2; i < nums.length; i++) {
    dp[i] = Math.max(nums[i] + dp[i - 2], dp[i - 1]);
    // profit = Math.max(dp[i], profit);
  }

  //   return profit;
  return dp[nums.length - 1];
};
// console.log(rob([2, 1, 1, 2]));
// console.log(rob([1, 2]));

//740. Delete and Earn
var deleteAndEarn = function (nums) {
  //Manually delete nums[i], will get nums[i] points, then will automatically delete ALL nums[i]-1, nums[i] +1
  //HOW:
  //similiar to robber, avoid steal adjacent house, in here: only earn point[i-1] or [i-2] + cur
  if (nums == null || nums.length == 0) return 0;

  //dic map {num:freq}
  const dic = new Array(Math.max(...nums) + 1).fill(0);

  //store dic
  for (let n of nums) {
    dic[n] += n;
  }

  const dp = new Array(Math.max(...nums) + 1).fill(0);
  //[2,1,1,2] in robber problem
  let profit = 0;
  //init dp
  dp[0] = dic[0];
  dp[1] = Math.max(dp[0], dic[1]);
  dp[2] = Math.max(dp[1], dic[2]);
  if (dic.length <= 2) {
    return dp[1];
  }
  if (dic.length <= 3) {
    return dp[2];
  }

  for (let i = 3; i < dic.length; i++) {
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + dic[i]);
    profit = Math.max(dp[i], profit);
  }
  return profit;
};
// console.log(deleteAndEarn([1]));

//213. House Robber II
var rob2 = function (nums) {
  //two pointe:[1,2,3,1] 1:1+3(4) 2:2+1(3)
  //first=[0] to [len-1] dp1=> profit second=[1] to [len] dp2=> profit, compare two profits
  if (nums.length == 1) return nums[0];
  if (nums == null || nums.length == 0) return 0;
  if (nums.length == 2) return Math.max(nums[0], nums[1]);

  const first = new Array(nums.length).fill(0);
  let p1 = 0;
  first[0] = nums[0];
  first[1] = Math.max(first[0], nums[1]);

  for (let i = 2; i < nums.length - 1; i++) {
    first[i] = Math.max(first[i - 1], first[i - 2] + nums[i]);
    p1 = Math.max(p1, first[i]);
  }
  const second = new Array(nums.length).fill(0);
  let p2 = 0;
  second[1] = nums[1];
  second[2] = Math.max(second[1], nums[2]);

  if (nums.length == 3) return Math.max(first[1], second[2]);
  for (let i = 3; i < nums.length; i++) {
    second[i] = Math.max(second[i - 1], second[i - 2] + nums[i]);
    p2 = Math.max(p2, second[i]);
  }

  return Math.max(p1, p2);
};
console.log(rob2([1, 2, 3, 1]));
console.log(rob2([1, 2, 3]));
console.log(rob2([1, 1]));
