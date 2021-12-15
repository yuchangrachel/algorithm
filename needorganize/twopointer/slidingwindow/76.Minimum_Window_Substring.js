/*
Minimum Window Substring

Window size changeable
*/
const minWindow = function (s, t) {
  //corner case check input valid or not
  if (s == null || t == null || s.length < t.length) return "";

  //because contains lower and uppercase
  const hash = new Array(256).fill(0);
  //store t into hash
  for (let i = 0; i < t.length; i++) {
    hash[t.charCodeAt(i)]++;
  }

  let left = 0,
    count = 0,
    max = s.length + 1; //avoid s='a', t='a' will ->""
  let res = "";
  for (let right = 0; right < s.length; right++) {
    //update hash
    hash[s.charCodeAt(right)]--;

    //check&update valid
    if (hash[s.charCodeAt(right)] >= 0) count++;

    //move left
    //keep removing uncessary: not exist or cur replace it
    //here not need handle count
    while (left < right && hash[s.charCodeAt(left)] < 0) {
      //not need to deduct count since scan from left to right, won't consider left anymore
      hash[s.charCodeAt(left)]++; //recover
      left++;
    }

    //result
    if (count == t.length && max > right - left + 1) {
      //must max > right -left+1,if =,nothing change, then cannot get into this statement
      max = right - left + 1;
      res = s.substring(left, right + 1);
    }
  }
  return res;
};

console.log(minWindow("ADOBECODEBANC", "ABC")); //"BANC"
/*
'''
    1.sliding window, window size is changable
    2.hash store t {char: frq}
    3.count,left
    '''
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s): return ""
        
        dic = collections.defaultdict(int)
        for c in t:
            dic[c] += 1
        
        count = 0
        left = 0
        res = ""
        max_len = len(s) + 1 #check if meet, if not return "" but len(s) still valid since s = t
        for i in range(len(s)):
            # update hash
            dic[s[i]] -= 1
            
            #valid
            if dic[s[i]] >= 0:
                count += 1
                
            # move left
            while left < i and dic[s[left]] < 0:
                dic[s[left]] += 1
                left += 1
            
            if count == len(t) and i - left + 1 < max_len:
                max_len = i - left + 1
                res = s[left: i+1]
                
        if max_len == len(s) + 1:
            return ""
        else:
            return res
        
*/
