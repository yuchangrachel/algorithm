var postorderTraversal = function (root) {
  let res = [];
  postorder(root, res);
  return res;
};

const postorder = function (root, res) {
  if (root === null) return;
  postorder(root.left, res);
  postorder(root.right, res);
  res.push(root.val);
};

//reverse preoder's result array
var postorderTraversal = function (root) {
  if (root === null) return [];

  const stack = [root];
  const res = [];

  while (stack.length > 0) {
    let top = stack.pop();
    res.push(top.val);

    if (top.left) stack.push(top.left);
    if (top.right) stack.push(top.right);
  }

  return res.reverse();
};
