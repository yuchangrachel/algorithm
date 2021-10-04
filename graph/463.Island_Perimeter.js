//find 1 and then spread out, dfs
var islandPerimeter = function (grid) {
  //corner case
  if (
    grid == null ||
    grid[0] == null ||
    grid.length == 0 ||
    grid[0].length == 0
  )
    return 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] == 1) {
        //find one unique island return result right away
        return helper(grid, i, j); //will do dfs find only one unique result
      }
    }
  }
  return 0;
};

const helper = function (grid, i, j) {
  //base case or terminate case reach boundary or water mean reach edge return 1
  if (
    i < 0 ||
    i >= grid.length ||
    j < 0 ||
    j >= grid[0].length ||
    grid[i][j] == 0
  )
    return 1;

  //visited cannot count again,so return 0
  if (grid[i][j] == 2) return 0;

  //this is part of island
  grid[i][j] = 2;

  //four directions
  return (
    helper(grid, i, j + 1) +
    helper(grid, i, j - 1) +
    helper(grid, i + 1, j) +
    helper(grid, i - 1, j)
  );
};
