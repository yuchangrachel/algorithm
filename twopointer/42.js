/*
42. Trapping Ran Water
Given n non-negative integers representing an elevation map 
where the width of each bar is 1, 
compute how much water it can trap after raining.
*/

//find peakindex
//leftmostbar moving right if higher,set high bar;otherwise smaller, store water
//rightmostbar moving left ...
var trap = function (height) {
  if (height == null || height.length == 0) return 0;

  //find peakindex
  let peak_index = 0;
  for (let i = 0; i < height.length; i++) {
    if (height[i] > height[peak_index]) {
      peak_index = i;
    }
  }

  //left
  let leftmostbar = 0;
  let water = 0;
  for (let i = 0; i < peak_index; i++) {
    if (height[i] > leftmostbar) {
      leftmostbar = height[i];
    } else {
      water += leftmostbar - height[i];
    }
  }

  //right
  let rightmostbar = 0;
  for (let i = height.length - 1; i > peak_index; i--) {
    if (height[i] > rightmostbar) rightmostbar = height[i];
    else water += rightmostbar - height[i];
  }

  return water;
};
