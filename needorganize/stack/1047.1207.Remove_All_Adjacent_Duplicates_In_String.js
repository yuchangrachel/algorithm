//1047
var removeDuplicates = function (s) {
  if (s == null || s.length == 0) return "";
  let stack = [];
  for (let c of s) {
    if (c == stack[stack.length - 1]) {
      stack.pop();
    } else {
      stack.push(c);
    }
  }
  return stack.join("");
};

//1209
var removeDuplicates = function (s, k) {
  if (s.length < k) return s;
  let stack = []; //stack[[char,count]]
  for (let c of s) {
    if (stack.length > 0 && stack[stack.length - 1][0] == c) {
      //must check stack.length> 0 then check if has stack top ele
      //not meet k, add+1
      stack[stack.length - 1][1]++;
      //meet k adjacent duplicate remove this inner array
      if (stack[stack.length - 1][1] == k) stack.pop();
    } else {
      //new char
      stack.push([c, 1]);
    }
  }

  //flatten 2d array
  let res = "";
  for (let [char, count] of stack) {
    res += char.repeat(count);
  }
  return res;
};
