/**
 * Definition for isBadVersion()
 *
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function (isBadVersion) {
  /**
   * @param {integer} n Total versions
   * @return {integer} The first bad version
   */
  return function (n) {
    //corner case
    if (n == 0) return 0;
    let low = 1;
    let high = n;
    while (low < high) {
      let mid = parseInt((low + high) / 2);
      if (isBadVersion(mid)) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    if (high != -1) {
      //low also ok
      return high;
    }
    return -1;
  };
};

/*
JS KNOWLEDGE:
Closure: work for nested function, inner func can use outer func's parameter
See sorted list: think binary search
See binary search: think boundary 
*/
