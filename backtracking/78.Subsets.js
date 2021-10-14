/*
                 []
                 /\
               [1] [2] ...
              /   \ 
            [1,2] [1,3]
            /
         [1,2,3]       
COMPELEXITY:T:O(N*2^N) S:O(N) not include output array(2^N)
*/
const subset = function (arr) {
  if (arr == null || arr.length == 0) return [[]];
  const res = [];
  dfs(0, [], res, arr);
  return res;
};
const dfs = function (start, inner, res, arr) {
  res.push([...inner]); //shadow copy keep updating this inner, but use copy one
  for (let i = start; i < arr.length; i++) {
    inner.push(arr[i]);
    dfs(i + 1, inner, res, arr);
    inner.pop();
  }
};
console.log(subset([1, 2, 3]));
