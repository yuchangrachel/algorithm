var repeatedSubstringPattern = function (s) {
  /*
    TOPIC:
    pattern size must <= s/2
    input s can be "bbb" or "ababab", so think how many times pattern appear
    1.search from mid, narrow pattern size ,check if s.length % i, if !=0, continue, narrow down pattern size
    2.count for substring, *, then see if == input s
    */
  if (s == null || s.length == 0) return false;

  for (let i = parseInt(s.length / 2); i >= 1; i--) {
    //reach 1, not 0, if single char->false
    if (s.length % i == 0) {
      let count = s.length / i;
      let temp = "";
      let substr = s.slice(0, i);
      for (let c = 0; c < count; c++) {
        temp += substr;
      }
      if (temp == s) return true;
    }
  }
  return false;
};
