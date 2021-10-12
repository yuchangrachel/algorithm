/*
COMPLEXITY:
S:O(m*n) for temp + O(c*r) for result
T:O(m*n) for convert 2d mat into 1d + O(r*c) store into result
*/
var matrixReshape = function (mat, r, c) {
  if (r == 0 || c == 0 || r * c != mat.length * mat[0].length) return mat; //return original matrix

  //flatten mat to 1D array
  let temp = new Array(mat.length * mat[0].length).fill(0);
  let index = 0; //tracking index for temp 1d array
  for (let i = 0; i < mat.length; i++) {
    for (let j = 0; j < mat[0].length; j++) {
      temp[index++] = mat[i][j];
    }
  }

  //create new matrix r*c
  let res = new Array(r).fill(0);
  for (let i = 0; i < res.length; i++) {
    res[i] = new Array(c).fill(0);
  }
  //store
  //reset index start over
  index = 0;
  for (let i = 0; i < r; i++) {
    for (let j = 0; j < c; j++) {
      res[i][j] = temp[index++];
    }
  }
  return res;
};

console.log(
  matrixReshape(
    [
      [1, 2],
      [3, 4],
    ],
    2,
    4
  )
);
