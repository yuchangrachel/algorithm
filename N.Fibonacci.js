//509
/*
1WAY recursion
COMPLEXITY: 
Not follow master theorem:T(n)=aT(n/b)+f(n) a>=1 and b > 1
use recurrence tree:f(n-1)+f(n-2)
=>T(n)=T(n-1)+T(n-2)+1 = 2T(n-2)+1
       1              n*1
     /   \
  n-2     n-2         2^1*(n-2)
 /   \
n-4  n-4              2^2*(n-4)
.....
1   1                 2^(n/2)*(1)
total need T:O(2^n)

For Fibonacci recursive implementation or any recursive algorithm, 
the space required is proportional to the maximum depth of the recursion tree, 
because, that is the maximum number of elements that can be present in the implicit function call stack.
      F6
      /\
    F4     F5
    /\     /\
   F2 F3   F3 F4
  /\  /\   /\ /\
 f0f1 f1f2 f1f2 f2 f3
                   /\
                   f1 f2
S:O(n)
*/
const fib = function (n) {
  if (n == 0) return 0;
  if (n == 1) return 1;
  return fib(n - 1) + fib(n - 2);
};

/*
2WAY iterative 
COMPLEXITY: T:O(n) S:O(1)
0 1 2       3...n
    f0s1
0 1 1       2
*/
var fib = function (n) {
  if (n < 2) return n;
  let first = 0;
  let second = 1;
  for (let i = 1; i < n; i++) {
    [first, second] = [second, first + second];
  }
  return second;
};

//3WAYbottom-top dp
var fib = function (n) {
  if (n <= 1) return n;
  const dp = new Array(n + 1).fill(0);
  dp[1] = 1;
  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  return dp[n];
};
