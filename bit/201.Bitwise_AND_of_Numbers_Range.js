/*
LOGIC:
1.find most siginficant bit's position(index-0, right to left) for startNum and endNum eg. 2:10(pos:1) 5:101(pos:2)
2.If positions of MSB are different, then result is 0. 
3.If positions are same. Let positions be msb_p. 
……a) We add 2msb_p to result. 
……b) We subtract 2msb_p from x and y, 
……c) Repeat steps 1, 2 and 3 for new values of x and y.
 
*/
const rangeBitwiseAnd = function (x, y) {
  let res = 0; // Initialize result

  while (x > 0 && y > 0) {
    // Find positions of MSB in x and y most siginificant bit(leftmost)
    let msb_p1 = msbPos(x);
    let msb_p2 = msbPos(y);

    // If positions are not same, return res
    if (msb_p1 != msb_p2) break;

    // Add 2^msb_p1 to result
    let msb_val = 1 << msb_p1; //shift 1 to msb_p1(2): mean 1 0 0 =4
    res = res + msb_val;

    // subtract 2^msb_p1 from x and y
    x = x - msb_val;
    y = y - msb_val;
  }

  return res;
};

function msbPos(n) {
  let msb_p = -1;
  while (n > 0) {
    n = n >> 1;
    msb_p++;
  }

  return msb_p;
}

console.log(rangeBitwiseAnd(1, 5));
