//substring, longest keyword, let me think about two pointer:sliding window
var lengthOfLongestSubstring = function (s) {
  //corner case invalid input
  if (s == null || s.length == 0) return 0;

  //use hash/array data structure store window's unqiue characters
  const hash = new Array(256).fill(0);

  //declare variable
  //result, prev pointer is starting pointer of window, later i is ending pointer of window
  let res = 0;

  for (let i = 0, prev = 0; i < s.length; i++) {
    //update hash
    hash[s.charCodeAt(i)]++;

    //move left pointer determine if need moving window to the right
    while (hash[s.charCodeAt(i)] > 1) {
      //duplicate in window,must delete prev one eg.abcc, we dont need duplicate in which index during window, so use while
      hash[s.charCodeAt(prev)]--;
      prev++;
    }

    //update res
    res = Math.max(res, i - prev + 1);
  }

  return res;
};
