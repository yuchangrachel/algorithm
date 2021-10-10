//dfs, if find incomplete word, recover it, keep find others until traverse all cells
var exist = function (board, word) {
  //corner case
  if (board == null || board[0] == null || word == null || word.length == 0)
    return false;

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (dfs(board, i, j, 0, word)) return true;
    }
  }
  return false;
};

const dfs = function (board, i, j, wi, word) {
  //base case or terminate case
  if (
    i < 0 ||
    i >= board.length ||
    j < 0 ||
    j >= board[0].length ||
    board[i][j] == "#" ||
    board[i][j] != word[wi]
  )
    return false;

  if (wi == word.length - 1) return true; //board[i][j] = word[wi] this is last char in word

  //now valid, let cur as visit, store it first, if in the end find it recover
  let temp = board[i][j];
  board[i][j] = "#";

  //recursion
  let found =
    dfs(board, i + 1, j, wi + 1, word) ||
    dfs(board, i - 1, j, wi + 1, word) ||
    dfs(board, i, j + 1, wi + 1, word) ||
    dfs(board, i, j - 1, wi + 1, word);

  // backtrack
  board[i][j] = temp;

  return found;
};
