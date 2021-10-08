/*
#340 #159
Longest Substring with AtMost Two DistinctCharacters
Longest substring with atMost K distinct Characters

/*
REFER:https://www.1point3acres.com/bbs/thread-544207-1-1.html

LOGIC:
    1.Iterate s in the meanwhile update hashtable{c:freq}with size 2
    2.When move left pointer: if hashmap is full, remove [left]
    3.substring result(right -left + 1)
    4.Window size(hash size) is fixed

KNOWELDGE:
python, JS map usage
Complexity: T:O(n^2) S: O(n)
  */
const lengthOfLongestSubstringTwoDistinct = function (s) {
  if (s == null || s.length == 0) return 0;

  //create hashtable control window, size is 2. can use map or array
  const dic = new Map();

  //create variable
  let res = 0,
    left = 0;

  //iterate s
  for (let i = 0; i < s.length; i++) {
    //store into hash, then check later if > k, move left
    dic.set(s[i], (dic.get(s[i]) || 0) + 1);

    //move left
    while (dic.size > 2) {
      if (dic.get(s[left]) > 1) dic.set(s[left], dic.get(s[left]) - 1);
      else dic.delete(s[left]);
      left++;
    }

    //update res since need longest substring so put here before move left
    res = Math.max(res, i - left + 1);
  }
  return res;
};

console.log(lengthOfLongestSubstringTwoDistinct("abddddbcccccc")); //7

//159
def lengthOfLongestSubstringKDistinct(s, k):
        if not k or not s or k == 0 or len(s) == 0: return 0

        dic = {}
        res = 0
        left = 0
        for i in range(len(s)):
            # store into hash
            dic[s[i]] = dic.get(s[i], 0) + 1

            # if hash size > k
            while len(dic) > k:
                if dic[s[left]] > 1: dic[s[left]]= dic.get(s[left]) - 1
                else: del dic[s[left]]
                left+=1
        
            # update res
            res = max(res, i - left +1)
        return res

print(lengthOfLongestSubstringKDistinct("eceba", 3))

