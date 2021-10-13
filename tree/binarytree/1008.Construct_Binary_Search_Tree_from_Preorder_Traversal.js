/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @return {TreeNode}
 
 LOGIC:
 1.convert array into BST
 2.How to anaylze array: arr[0] = root
 3.How to build tree: new TreeNode(v) and do recursion
 */
var bstFromPreorder = function (preorder) {
  //corner case
  if (preorder == null || preorder.length == 0) return null;

  let root = new TreeNode(preorder[0]);
  let i = 1;
  //find leftsubtree and rightsubtree
  while (i < preorder.length && preorder[i] < preorder[0]) {
    i++; //[5,1,7] and [10,12]
  }
  root.left = bstFromPreorder(preorder.slice(1, i));
  root.right = bstFromPreorder(preorder.slice(i));

  return root;
};
