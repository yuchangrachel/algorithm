/*
Explain: Check need how many index after cur index, to get bigger number than cur
1.brute force:O(n^2)
*/
var dailyTemperatures = function (temperatures) {
  //corner
  if (temperatures == null || temperatures.length == 0) return [];
  if (temperatures.length == 1) return [0]; //no future day

  const res = [];
  for (let i = 0; i < temperatures.length - 1; i++) {
    let cur = temperatures[i];
    for (let j = i + 1; j < temperatures.length; j++) {
      if (temperatures[j] > cur) {
        res.push(j - i);
        break;
      }
      //already reach last index, still no warmer one
      if (j == temperatures.length - 1) res.push(0);
    }
  }
  res.push(0);
  return res;
};
//2.Stack worse case O(n^2) but more efficient since check while loop, if will enter or not
var dailyTemperatures = function (temperatures) {
  const stack = []; //store temp' s index
  const days = new Array(temperatures.length).fill(0);

  for (let i = 0; i < temperatures.length; i++) {
    while (
      stack.length > 0 &&
      temperatures[stack[stack.length - 1]] < temperatures[i]
    ) {
      //one warmer one can use to many previous temps
      let last = stack.pop();
      days[last] = i - last;
    }
    stack.push(i);
  }
  return days;
};

console.log(dailyTemperatures2([73, 74, 75, 71, 69, 72, 76, 73]));
