// Number of provinces
var findCircleNum = function (isConnected) {
  //TOPIC: same as Friend Circle, similiar to Number of isLand

  if (isConnected == null || isConnected.length == 0) return 0;

  let province = 0;

  for (let i = 0; i < isConnected.length; i++) {
    for (let j = 0; j < isConnected[0].length; j++) {
      if (isConnected[i][j] == 1) {
        dfs(i, j, isConnected);
        province++;
      }
    }
  }
  return province;
};

const dfs = function (i, j, grid) {
  if (
    i < 0 ||
    j < 0 ||
    i >= grid.length ||
    j >= grid[0].length ||
    grid[i][j] != 1
  )
    return;
  grid[i][j] = 0;
  grid[j][i] = 0;
  //handle indirect relation
  //next row different column
  for (let k = 0; k < grid[0].length; k++) {
    if (grid[j][k] == 1) dfs(j, k, grid);
  }
};
