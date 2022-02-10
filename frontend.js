/*
1.remove characters:Given a string contaning only a, b and c, remove all b and ac.
*/
//1WAY Stack
function removeChars(input) {
  // your code here
  const stack = []
  for (let c of input){
    if (c === 'a'){
      stack.push(c)
    }
    else if (c === 'c'){
      if (stack.length && stack[stack.length-1] === 'a'){
        stack.pop()
      }
      else{
        stack.push(c)
      }
    }
  }
  return stack.join("")
}

