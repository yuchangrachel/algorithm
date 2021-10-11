//https://leetcode.com/discuss/interview-question/406135/ibm-oa-2019-aladdin-and-his-carpet-backend
/*
LOGIC:
1.how to find mini start index for circular path? since need finish whole arr, so use total count whole journey
2.check accu magic enough for dis,if not, update start point and reset accumagic
*/
const optimalPoint = function (magic, dist) {
  let start = -1;
  let accuMagic = 0;
  let total = 0;
  for (let i = 0; i < magic.length; i++) {
    total += magic[i] - dist[i];
    accuMagic += magic[i] - dist[i];
    if (accuMagic < 0) {
      //update start
      accuMagic = 0;
      start = i;
    }
  }
  if (total >= 0) return start + 1;
  else return -1;
};

console.log(optimalPoint([2, 10, 10, 30], [1, 10, 12, 5])); //3
console.log(optimalPoint([2, 4, 5, 2], [4, 3, 1, 3]));
