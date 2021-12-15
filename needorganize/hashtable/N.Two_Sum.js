//1.Two Sum: simple hashmap

//167. Two Sum II - Input array is sorted: simple binary search

//1099.Two Sum Less Than K
/*
Given an array A of integers and integer K, return the maximum S 
such that there exists i < j with A[i] + A[j] = S and S < K. 
If no i, j exist satisfying this equation, return -1.
Example 1:
Input:A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:
Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.
Note:
1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
*/
/*
LOGIC:
1.sort ls, binary search, [low]+[high] compare with K

COMPELEXITY: T:O(nlogn)
*/
const twosumlessthanK = function (ls, K) {
  if (ls == null || ls.length == 0 || K == 0) return 0;

  //in js, must write arrow function
  ls.sort((a, b) => a - b);
  let low = 0,
    high = ls.length - 1,
    res = -1;
  while (low < high) {
    //no = since no searching target, only range
    if (ls[low] + ls[high] >= K) high--;
    else {
      res = Math.max(res, ls[low] + ls[high]);
      low++;
    }
  }
  return res;
};
console.log(twosumlessthanK([34, 23, 1, 24, 75, 33, 54, 8], 60));
console.log(twosumlessthanK([20, 10, 30], 15));

//653.1214. Two Sum IV - Input is a BST
/*
LOGIC:
1.Same as Two sum in array, but now in tree, search tree
2.Search Tree: two general ways: dfs(pre-order, in-order, post-order, level-order search)
3.use array store node.val, no need hash, no need k-v pair, since find result return right away

COMPLEXITY:
T:O(1/2n) S:O(logn)
*/
var findTarget = function (root, k) {
  return preorder(root, k, []); //this traverse in this case return something
};

const preorder = function (root, k, dic) {
  //base case or terminate case
  if (root == null) return false;

  if (dic.includes(k - root.val)) return true;
  dic.push(root.val);
  return preorder(root.left, k, dic) || preorder(root.right, k, dic);
};

//170.Two sum iii- data structure design
// class TwoSum:
//     """
//     @param number: An integer
//     @return: nothing
//     """
//     # create array store added numbers, since no need index pair
//     nums = []
//     def add(self, number): # O(1)
//         self.nums.append(number)
//     """
//     @param value: An integer
//     @return: Find if there exists any pair of numbers which sum is equal to the value.
//     """
//     def find(self, value): # O(nlogn)
//         if not self.nums or len(self.nums) == 0: return False
//         self.nums.sort()
//         low = 0
//         high = len(self.nums) - 1
//         while low < high: #find target, but two number needed o(logn)
//             if self.nums[low] + self.nums[high] > value:
//                 high -=1
//             elif self.nums[low] + self.nums[high] < value:
//                 low +=1
//             else:
//                 return True
//         return False
