var allPathsSourceTarget = function (graph) {
  /*
    TOPIC: Findd all valid paths(USING Backtracking)
    graph is 2d array, graph[index], index has pointed nodes:graph[index] result; eg. graph[0]  =[1,2] (means 0 point to 1 and 2)
    index1 point to 3, index2 point to 3. 
    FIND graph.length == n(node)
    */
  if (
    graph == null ||
    graph[0] == null ||
    graph.length == 0 ||
    graph[0].length == 0
  )
    return [];
  const res = [];
  const inner = [0];

  helper = function (index) {
    if (index === graph.length - 1) {
      res.push([...inner]);
      return;
    }
    for (let next of graph[index]) {
      inner.push(next);
      helper(next);
      inner.pop();
    }
  };
  helper(0);

  return res;
};
