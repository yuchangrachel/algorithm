/*
LOGIC:
check if valid sudoku
1th rule: each one compare their rows 
2th rule: each one compare their columns
3th rule: nine 3by3 subboxes
see if there is duplicates, can use set 
*/
var isValidSudoku = function (board) {
  //corner case
  if (
    board == null ||
    board[0] == null ||
    board.length != 9 ||
    board[0].length != 9
  )
    return false;

  //compare whole rows
  for (let row = 0; row < 9; row++) {
    const row_set = new Set(); //new column will have new set
    for (let col = 0; col < 9; col++) {
      if (board[row][col] == ".") continue;
      else {
        if (row_set.has(board[row][col])) return false;
        else row_set.add(board[row][col]);
      }
    }
  }

  //compare whole columns
  for (let col = 0; col < 9; col++) {
    const col_set = new Set();
    for (let row = 0; row < 9; row++) {
      if (board[row][col] == ".") continue;
      else {
        if (col_set.has(board[row][col])) return false;
        else col_set.add(board[row][col]);
      }
    }
  }

  //compare subboxes
  for (let box = 0; box < 9; box++) {
    const box_set = new Set();
    for (let row = 0; row < 3; row++) {
      for (let col = 0; col < 3; col++) {
        let cur = board[row + 3 * parseInt(box / 3)][col + 3 * (box % 3)];
        if (cur !== ".") {
          if (box_set.has(cur)) return false;
          else box_set.add(cur);
        }
      }
    }
  }
  return true;
};
console.log(
  isValidSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
  ])
);
//true
