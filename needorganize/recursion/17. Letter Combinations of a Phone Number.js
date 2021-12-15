var letterCombinations = function (digits) {
  /*
    hardcore map{num:[char]}
    TOPIC:recursion for combination 
    Each combination size is same as digit.len
    Time Complexity : O(3^m * 4^n) average, worst:"7979":4^(4*4)
    */
  if (digits == null || digits.length == 0) return [];

  const phones = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]; //0-7 (2-9)
  const res = [];

  dfs = function (index, prev) {
    if (index == digits.length) {
      res.push(prev);
      return;
    } else {
      let getIndex = digits[index] - "2";
      let choice = phones[getIndex];
      for (let i = 0; i < choice.length; i++) {
        dfs(index + 1, prev + choice[i]);
      }
    }
  };
  dfs(0, "");
  return res;
};
