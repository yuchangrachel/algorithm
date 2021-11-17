//290. Word Pattern

var isIsomorphic = function (s, t) {
  //TOPIC: CHECK if two strings in same pattern, see both are same length, duplicate char also in same pos
  //HOW: use map store{char: updating index}

  if (
    s.length != t.length ||
    s == null ||
    t == null ||
    s.length == 0 ||
    t.length == 0
  )
    return false;

  const dic1 = new Array(256).fill(0);
  const dic2 = new Array(256).fill(0);

  for (let i = 0; i < s.length; i++) {
    if (dic1[s[i].charCodeAt()] != dic2[t[i].charCodeAt()]) return false;
    else {
      dic1[s[i].charCodeAt()] += 1;
      dic2[t[i].charCodeAt()] += 1;
    }
    console.log(dic1, " ", dic2);
  }
  return true;
};
console.log(isIsomorphic("foo", "bar"));
