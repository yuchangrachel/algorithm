/*
LOGIC:
1.Create 2d array and add elements layer by layer 
2.when ith layer, will add[0]=1, [i][j] = [i-1][j-1]+[i-1][j]
*/
var generate = function (numRows) {
  if (numRows == 0) return [[]];

  const res = [];
  for (let i = 0; i < numRows; i++) {
    //layer by layer
    //create inner array
    const inner = new Array(i + 1).fill(1);
    for (let j = 1; j < inner.length - 1; j++) {
      //skip first and last
      if (i == 3) {
        console.log(res[i - 1][j - 1], " ", res[i - 1][j]);
      }
      inner[j] = res[i - 1][j - 1] + res[i - 1][j];
    }
    res.push(inner);
  }
  return res;
};

console.log(generate(5));
