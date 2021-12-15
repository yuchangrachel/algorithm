/*
Find common characters, all strings consist of lowercase english
*/
const twoStrings = function (a, b) {
  if (a == null || b == null || a.length == 0 || b.length == 0) return "No";

  //a b length is same
  for (let i = 0; i < a.length; i++) {
    let word1 = a[i];
    let word2 = b[i];

    //find shorter word, store set, since only find it, dont need count
    if (word1.length > word2.length) {
      let temp = word2;
      word2 = word1;
      word1 = temp;
    }
    let temp_set = new Set();
    let isCommon = false;
    for (let c of word1) {
      temp_set.add(c);
    }

    for (let c of word2) {
      if (temp_set.has(c)) {
        isCommon = true;
        console.log("Yes");
        break;
      }
    }

    if (isCommon == false) console.log("No");
  }
};

twoStrings(["hello", "hi", "", "33zq"], ["world", "bye", "a", "q"]);
