var generateParenthesis = function (n) {
  //Topic: Return display all results:RECURSION
  //Think invalid: )( : if leftremain > rightremain
  //recursion left -1, then right -1
  if (n == 0) return [];
  const res = [];
  dfs = function (leftremain, rightremain, str) {
    if (leftremain > rightremain) return;
    else if (leftremain == 0 && rightremain == 0) {
      res.push(str);
      return;
    } else {
      if (leftremain > 0) dfs(leftremain - 1, rightremain, str + "(");
      if (rightremain > 0) dfs(leftremain, rightremain - 1, str + ")");
    }
  };
  dfs(n, n, "");
  return res;
};
