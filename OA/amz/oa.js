// 1. BadNumbers： 给一个array of integers of bad numbers 和两个parameter upper bound 和 lower bound。
// 目的是找出最长的数组长度并且不含bad number。
// 例如：bad number = [2, 6, 5] lower = 1 upper = 10
// 那么【1】，【3, 4】，【7, 10】那么return 4 因为7 8 9 10是最长的 注意是Inclusive
/*
LOGIC:
bad number=[2,5,6]
whole number=[1,2,3,4,5,6,7,8,9,10]
*/
const badNumber = function (arr, low, high) {
  let res = 0;
  let left = low;
  for (let i = low; i <= high; i++) {
    if (!arr.includes(i)) {
      res = Math.max(res, i - left + 1);
    } else {
      left = i + 1;
    }
  }
  return res;
};
console.log(badNumber([2, 6, 5], 1, 10));
