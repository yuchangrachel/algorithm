//125
var isPalindrome = function (s) {
  let regex = new RegExp("^[a-zA-Z0-9]");
  s = s.toLowerCase().replace(regex, "");
  console.log(s);
  let copy = s;
  return copy.split("").reverse().join("") == s;
};

//680
