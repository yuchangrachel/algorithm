//1365. How Many Numbers Are Smaller Than the Current Number
var smallerNumbersThanCurrent = function (nums) {
  //1WAY O(n)
  //create counter[101]
  //create presum
  //res = presum[nums[i]]
  const counter = new Array(101).fill(0);
  for (let n of nums) {
    counter[n] += 1;
  }
  let sum = 0;
  const presum = new Array(101).fill(0);
  for (let i = 0; i < 101; i++) {
    presum[i] = sum;
    sum += counter[i];
  }
  const res = new Array(nums.length).fill(0);
  for (let i = 0; i < res.length; i++) {
    res[i] = presum[nums[i]];
  }
  return res;

  //2WAY USE built in sort method O(nlogn)
  // let copy = [...nums]
  // copy.sort((a,b)=> a-b)
  // const res = new Array(nums.length).fill(0)
  // for (let i = 0; i < nums.length; i++){
  //     res[i] = copy.indexOf(nums[i])
  // }
  // return res

  //3WAYbrute force O(n^2)
  // const res = new Array(nums.length).fill(0)
  // for (let i = 0; i < nums.length; i++){
  //     for(let j = 0; j < nums.length; j++){
  //         if (nums[j] < nums[i]){
  //             res[i] += 1
  //         }
  //     }
  // }
  // return res
};
