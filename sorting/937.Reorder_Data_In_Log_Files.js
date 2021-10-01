/*
937. Reorder Data in Log Files

You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.
There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.
Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

*/

/*
KNOWLEDGE
aStr.localCompare(bStr)
aStr < bStr in aphabet order: -1
aStr > bStr: 1
aStr = bStr: 0
*/
//find pattern: each string[0] will be ignored
//how to identify letter log or digit log: string[last] is char or digit set two group, then add both
//sort them separate

var reorderLogFiles = function (logs) {
  if (logs == null || logs.length == 0) return [];

  //creat two array for one digit group and another letter group
  const digits = [];
  const letters = [];
  for (let log of logs) {
    if (!isNaN(log[log.length - 1])) {
      //it is digit log
      digits.push(log);
    } else {
      letters.push(log);
    }
  }

  // sort letters perspectively
  letters.sort((a, b) => {
    let strA = a.substr(a.indexOf(" ") + 1);
    let strB = b.substr(b.indexOf(" ") + 1);

    if (strA === strB) return a.localeCompare(b);
    else return strA.localeCompare(strB);
  });

  // push them together and return
  return [...letters, ...digits];
};
