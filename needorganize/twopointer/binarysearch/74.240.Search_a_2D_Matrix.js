//74
//sort and search target: binary search
//T:O(mlogn) slower
var searchMatrix = function (matrix, target) {
  if (
    matrix == null ||
    matrix[0] == null ||
    matrix.length == 0 ||
    matrix[0].length == 0
  )
    return false; //no result

  for (let row of matrix) {
    if (target >= row[0] && target <= row[matrix[0].length - 1]) {
      //find target row, now doing binary search
      let low = 0,
        high = matrix[0].length - 1;
      while (low <= high) {
        //need find target so <=
        let mid = parseInt((low + high) / 2);
        if (row[mid] == target) return true;
        //find it
        else if (row[mid] < target) low = mid + 1;
        else high = mid - 1;
      }
    }
  }
  return false;
};

//log(mn)
//sort and search target: binary search
/*
LOGIC:
1.sorted 2d matrix, do binary search
2.low set 0, high set m*n(higher), so while (low < high)
3.process cell[i][j], real row = mid/coltotal#, real col = mid%coltotal#
*/
var searchMatrix = function(matrix, target) {
    if (matrix == null || matrix[0] == null || matrix.length  == 0 || matrix[0].length == 0) return false
    let low = 0, high = matrix.length * matrix[0].length
    while (low < high){ //!= since high add extra 1
        let mid = parseInt((low + high) / 2)
        //process cell[i][j]
        let i = parseInt(mid/matrix[0].length) //row /coltotal#!!! not rowtotal# eg.[[1,1]] 0
        let j =mid % matrix[0].length //column %coltotal#
        if (matrix[i][j] == target) return true
        else if (target > matrix[i][j]) low = mid + 1
        else high = mid 
    }
    return false
};

//240.Search a 2D Matrix II
//O(m+n) maximum path is one row plus one column
var searchMatrix = function (matrix, target) {
  if (
    matrix == null ||
    matrix[0] == null ||
    matrix.length == 0 ||
    matrix[0].length == 0
  )
    return false;

  //start point(top-right) i tracking rows, j tracking cols
  let i = 0,
    j = matrix[0].length - 1;
  while (i < matrix.length && j >= 0) {
    if (matrix[i][j] == target) return true;
    else if (matrix[i][j] < target) {
      i++;
    } else {
      j--;
    }
  }
  return false;
};
