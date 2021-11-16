//844. Backspace String Compare
var backspaceCompare = function (s, t) {
  //REFER YOUTUBE
  //TOPIC:each # means backspace, may delete one char in fron of #, after all #, then compare s and t see if they are equal
  //2WAY TWO POINTER S:O(1)
  let sp = s.length - 1;
  let tp = t.length - 1;
  let h1 = 0;
  let h2 = 0;

  while (sp >= 0 || tp >= 0) {
    //need both reach index0
    while (sp >= 0) {
      if (s[sp] == "#") {
        h1++;
        sp--;
      } else if (h1 > 0) {
        h1--;
        sp--;
      } else {
        break;
      }
    }

    while (tp >= 0) {
      if (t[tp] == "#") {
        h2++;
        tp--;
      } else if (h2 > 0) {
        h2--;
        tp--;
      } else {
        break;
      }
    }

    if (sp >= 0 && tp >= 0 && s[sp] != t[tp]) return false;
    if (sp >= 0 && tp < 0) return false;
    if (sp < 0 && tp >= 0) return false;

    sp--;
    tp--;
  }

  return true;

  //1WAY(S:O(n)): use two stacks for s, t, store letter, see # pop
  //     if (s == "" && t == "") return true

  //     const s1 = []
  //     const s2 = []

  //     for (let ch of s){
  //         if (ch != "#"){
  //             s1.push(ch)
  //         }
  //         else{
  //             if (s1.length > 0){
  //                 s1.pop()
  //             }
  //         }
  //     }
  //     for (let ch of t){
  //         if (ch != "#"){
  //             s2.push(ch)
  //         }
  //         else{
  //             if (s2.length > 0){
  //                 s2.pop()
  //             }
  //         }
  //     }
  //     return s1.join("") == s2.join("")
};
console.log(backspaceCompare("xywrrmp", "xywrrmu#p"));
