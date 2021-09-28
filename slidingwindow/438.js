const asscii = "a".charCodeAt();

var findAnagrams = function (s, p) {
  //corner case or check input valid
  if (s.length < p.length) return [];

  //use data structure eg.array, map store specific elements in window {char: freq}
  const hash = new Array(26).fill(0);
  for (let i = 0; i < p.length; i++) {
    hash[p.charCodeAt(i) - asscii]++;
  }

  //declare result, left pointer(start of window), count(current situation)
  const res = [];
  let left = 0,
    count = 0;

  //loop for window right for expanding
  for (let right = 0; right < s.length; right++) {
    //now used it, so update(deduct amount in hash) if after deduct is -1, mean not in pstr
    hash[s.charCodeAt(right) - asscii]--;

    //check valid char in pstr
    if (hash[s.charCodeAt(right) - asscii] >= 0) {
      count++;
    }

    //check if need to move left, need keep window size is p length
    if (right > p.length - 1) {
      //add it again since deduct
      hash[s.charCodeAt(left) - asscii]++;
      //deduct count since was valid
      if (hash[s.charCodeAt(left) - asscii] > 0) {
        count--;
      }

      left++;
    }

    if (count == p.length) res.push(left);
  }
  return res;
};

console.log(findAnagrams("acba", "ab"));
