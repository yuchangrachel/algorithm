'''
CHECK SORTING ALGORITHM:
https://leetcode.com/problems/largest-number/discuss/53298/Python-different-solutions-(bubble-insertion-selection-merge-quick-sorts).   
1 WAY PY built-in method
    LOGIC:Customized sort
    String comparator and concatenate sorted strings
    1.'9'largest,sort by first digit,
    2.'34','30',if first digit is same, then sort second digit
    3.'3' '30': should 330, shouldn't 303 , so compare after a+b
    4.Edge case[0,0]=> '0'
    
    KNOWLEDGE:
    PYTHON: 
    higher order function:functools
    cmp_to_key compare iterable element while sorting 
'''
from functools import cmp_to_key
def largestNumber1(nums):
    def helper(a,b):
        # sorted by value of concatenated string increasingly
        if a+b > b+a: return 1
        elif a ==b: return 0
        else: return -1
    
    # convert num into string
    nums = [str(n) for n in nums]
    nums.sort(key=cmp_to_key(helper), reverse=True)
    
    #removing trailing leading 0 or only one 0
    # 1WAY return "".join(nums).lstrip('0') or '0'
    # 2WAY
    ans = '0' if nums[0] == '0' else ''.join(nums)
    return ans

'''
var largestNumber = function (nums) {
  const comparator = function (a, b) {
    let ab = a.toString() + b.toString();
    let ba = b.toString() + a.toString();
    return ba - ab;
  };

  let sortjoin = nums.sort(comparator).join("");
  console.log(nums);
  if (parseInt(sortjoin) === 0) return "0";
  else return sortjoin;
};

'''


print(largestNumber2([3,30,34,5,9]))
print(largestNumber2([0,0]))