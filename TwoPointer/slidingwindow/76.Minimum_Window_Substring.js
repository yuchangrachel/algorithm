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
'''
    TOPIC:find mini substring of s contains all chars in t(t order matter!)
    STEP:Sliding window,window size is fixed:widow is t
    1.store t as chararray 256{ch code:freq}
    2.iterate s, update chararray. handle valid, left, handle res(find min)
    3.corner case:"b" "a"=>"" "A" "A"=>"A"
    '''
    def minWindow(self, s: str, t: str) -> str:
        if s is None or t is None or len(t) > len(s): return ""
        # create chararray for t
        char = [0] * 256
        for c in t:
            char[ord(c)] += 1
        
        # set up variable
        left = 0
        res = s
        count = 0
        max_len = len(s) + 1 # think corner case
        
        # iterate s
        for i in range(len(s)):
            #update chararray
            char[ord(s[i])] -= 1
            
            #check valid
            if char[ord(s[i])] >= 0:
                count += 1
            
            #check left when invalid for left part
            while left < i and char[ord(s[left])] < 0:
                char[ord(s[left])] += 1 # recover
                left += 1
            
            #get res
            if count == len(t) and i - left + 1 < max_len:
                res = s[left:i+1]
                max_len = i - left + 1
            
        return "" if max_len == len(s) + 1 else res
        
